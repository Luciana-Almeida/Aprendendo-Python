from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import crud, schemas, models
from app.database import get_db
from fastapi_pagination import Page, add_pagination, paginate

router = APIRouter(
    prefix="/atletas",
    tags=["atletas"],
)

@router.get("/", response_model=Page[schemas.Atleta])
def get_atletas(
    nome: Optional[str] = Query(None, description="Nome do atleta"),
    cpf: Optional[str] = Query(None, description="CPF do atleta"),
    db: Session = Depends(get_db)
):
    atletas = crud.get_atletas(db, nome=nome, cpf=cpf)
    return paginate(atletas)

@router.post("/", response_model=schemas.Atleta, status_code=status.HTTP_201_CREATED)
def create_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_atleta(db, atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

add_pagination(router)
