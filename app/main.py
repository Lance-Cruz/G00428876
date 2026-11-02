from fastapi import Depends, HTTPException, FastAPI, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base, ClientDB
from app.schemas import ClientCreate, ClientRead

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post(
    "/api/loans",
    response_model=ClientRead,
    status_code=status.HTTP_201_CREATED,
)
def add_loan(
    new_loan: ClientCreate,
    db: Session = Depends(get_db),
):
    db_loan = ClientDB(**new_loan.model_dump())
    db.add(db_loan)
    try:
        db.commit()
        db.refresh(db_loan)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Loan already exists"
        )
    return db_loan

@app.get(
    "/api/loan/{id}",
    response_model=ClientRead,
)
def get_loan(id: int, db: Session = Depends(get_db)):
    db_loan = db.get(ClientDB, id)
    if db_loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )
    return db_loan