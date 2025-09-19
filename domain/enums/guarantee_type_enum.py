from enum import Enum


class GuaranteeTypeEnum(str, Enum):
    PERSONAL_CHEQUE = "personal-cheque"
    GUARANTOR_CHEQUE = "guarantor-cheque"
    TWO_CHEQUES = "two-cheques"
    GUARANTOR_SALARY_DEDUCTION = "guarantor-salary-deduction"