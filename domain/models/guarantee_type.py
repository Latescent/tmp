from typing import Optional


class GuaranteeType:
    def __init__(self, title: str, slug: str, max_loan_amount: int, **kwargs) -> None:
        self.id: Optional[int] = kwargs.get('id')
        self.title: str = title
        self.slug: str = slug
        self.max_loan_amount: int = max_loan_amount

    @classmethod
    def create(cls, title: str, slug: str, max_loan_amount: int):
        return cls(title=title, slug=slug, max_loan_amount=max_loan_amount)