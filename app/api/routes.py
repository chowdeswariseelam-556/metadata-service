
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.dataset import Dataset
from app.models.lineage import Lineage
from app.schemas.dataset import DatasetCreate, LineageCreate
from app.services.lineage_service import has_cycle

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/datasets")
def create_dataset(payload: DatasetCreate, db: Session = Depends(get_db)):
    dataset = Dataset(**payload.model_dump())
    db.add(dataset)
    db.commit()
    return {"message": "Dataset created"}

@router.post("/lineage")
def create_lineage(payload: LineageCreate, db: Session = Depends(get_db)):

    if has_cycle(db, payload.upstream_fqn, payload.downstream_fqn):
        raise HTTPException(status_code=400, detail="Cycle detected")

    lineage = Lineage(**payload.model_dump())
    db.add(lineage)
    db.commit()

    return {"message": "Lineage created"}

@router.get("/search")
def search(keyword: str, db: Session = Depends(get_db)):
    results = db.query(Dataset).filter(
        Dataset.fqn.like(f"%{keyword}%")
    ).all()

    return results
