from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..models import Vegetal as VegetalModel
from ..schemas import Vegetal, VegetalCreate, VegetalUpdate
from ..utils.security import get_current_active_user, get_current_gerente_user

router = APIRouter(
    prefix="/vegetais",
    tags=["vegetais"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=Vegetal, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_gerente_user)])
def create_vegetal(vegetal: VegetalCreate, db: Session = Depends(get_db)):
    db_vegetal = db.query(VegetalModel).filter(VegetalModel.nome == vegetal.nome).first()
    if db_vegetal:
        raise HTTPException(status_code=400, detail="Vegetal já registrado")
    
    db_vegetal = VegetalModel(**vegetal.dict())
    db.add(db_vegetal)
    db.commit()
    db.refresh(db_vegetal)
    return db_vegetal

@router.get("/", response_model=List[Vegetal])
def read_vegetais(skip: int = 0, limit: int = 100, ativo: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(VegetalModel)
    if ativo is not None:
        query = query.filter(VegetalModel.ativo == ativo)
    vegetais = query.offset(skip).limit(limit).all()
    return vegetais

@router.get("/{vegetal_id}", response_model=Vegetal)
def read_vegetal(vegetal_id: int, db: Session = Depends(get_db)):
    db_vegetal = db.query(VegetalModel).filter(VegetalModel.id == vegetal_id).first()
    if db_vegetal is None:
        raise HTTPException(status_code=404, detail="Vegetal não encontrado")
    return db_vegetal

@router.put("/{vegetal_id}", response_model=Vegetal, dependencies=[Depends(get_current_gerente_user)])
def update_vegetal(vegetal_id: int, vegetal: VegetalUpdate, db: Session = Depends(get_db)):
    db_vegetal = db.query(VegetalModel).filter(VegetalModel.id == vegetal_id).first()
    if db_vegetal is None:
        raise HTTPException(status_code=404, detail="Vegetal não encontrado")
    
    update_data = vegetal.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_vegetal, key, value)
    
    db.commit()
    db.refresh(db_vegetal)
    return db_vegetal

@router.delete("/{vegetal_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_current_gerente_user)])
def delete_vegetal(vegetal_id: int, db: Session = Depends(get_db)):
    db_vegetal = db.query(VegetalModel).filter(VegetalModel.id == vegetal_id).first()
    if db_vegetal is None:
        raise HTTPException(status_code=404, detail="Vegetal não encontrado")
    
    # Soft delete - apenas marca como inativo
    db_vegetal.ativo = False
    db.commit()
    return None
