import random
from application.loan.commands.create_loan_request_command import CreateLoanRequestCommand
from shared.unit_of_work import UnitOfWork
from domain.models.loan_request import LoanRequest
from domain.models.user import User


class CreateLoanRequestHandler:
    def __init__(self, uow: UnitOfWork, current_user: User):
        self.uow = uow
        self.current_user = current_user

    async def _generate_unique_loan_code(self, uow) -> str:
        """Generate a unique 8-digit loan code"""
        while True:
            loan_code = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            existing = await uow.loan_request_repo.get_by_loan_code(loan_code)
            if not existing:
                return loan_code

    async def handle(self, command: CreateLoanRequestCommand) -> None:
        async with self.uow as uow:
            # Get loan-status parent enumeration
            loan_status_parent = await uow.enumeration_repo.get_by_slug("loan-status")

            # Get pending status from enumerations
            pending_status = await uow.enumeration_repo.get_by_parent_id_and_slug(loan_status_parent.id, "pending")

            # Get guarantee type by slug
            guarantee_type = await uow.guarantee_type_repo.get_by_slug(command.guarantee_type)

            # Generate unique loan code
            loan_code = await self._generate_unique_loan_code(uow)

            # Create loan request
            loan_request = LoanRequest.create(
                user_id=self.current_user.id,
                loan_code=loan_code,
                amount=command.amount,
                status_id=pending_status.id,
                guarantee_type_id=guarantee_type.id,
                installment_count=command.installment_count,
                installment_amount=command.installment_amount,
                guarantor_id=command.guarantor_id
            )

            await uow.loan_request_repo.create(loan_request)
            await uow.commit()