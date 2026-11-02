from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

BorrowerStr = Annotated[str, StringConstraints(min_length=2, max_length=60)]
PurposeStr = Annotated[str, StringConstraints(min_length=5, max_length=100)]

class ClientCreate(BaseModel):
    equipment_id: int = Field(gt=0)
    borrower_name: BorrowerStr
    loan_days: int = Field(gt=0, lt=15)
    purpose: PurposeStr
    status: str = "PENDING"

class ClientRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    equipment_id: int = Field(gt=0)
    borrower_name: BorrowerStr
    loan_days: int = Field(gt=0, lt=15)
    purpose: PurposeStr
    status: str