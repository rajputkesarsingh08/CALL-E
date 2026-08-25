from typing import Any

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator


class CallPlanRequest(BaseModel):

    phone_number: str

    target: str

    purpose: str

    additional_instructions: str = ""

    preferred_outcome: str = ""

    @field_validator(
        "phone_number"
    )
    @classmethod
    def validate_phone(
        cls,
        value: str
    ):

        if not value.startswith("+"):
            raise ValueError(
                "Phone number must use E.164 format."
            )

        digits = value[1:]

        if not digits.isdigit():
            raise ValueError(
                "Phone number contains invalid characters."
            )

        if not 8 <= len(digits) <= 15:
            raise ValueError(
                "Invalid phone number length."
            )

        return value


class CallPlan(BaseModel):

    objective: str

    target: str

    questions: list[str]

    tone: str

    success_criteria: list[str]


class StartCallRequest(BaseModel):

    plan: CallPlan


class CallResponse(BaseModel):

    id: int

    phone_number: str

    target: str

    purpose: str

    status: str

    call_duration: int | None = None

    summary: str | None = None

    transcript: str | None = None

    structured_result: Any | None = None