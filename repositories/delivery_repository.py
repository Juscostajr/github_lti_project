from sqlalchemy.orm import Session
from domain.models import Delivery

def get_by_id(db: Session, delivery_id: int) -> Delivery | None:
    return db.query(Delivery).filter(Delivery.id == delivery_id, Delivery.is_active == True).first()

def create(db: Session, delivery: Delivery) -> Delivery:
    db.add(delivery)
    db.commit()
    db.refresh(delivery)
    return delivery

def list_by_activity(db: Session, activity_id: int) -> list[Delivery]:
    return db.query(Delivery).filter(Delivery.activity_id == activity_id, Delivery.is_active == True).all()

def soft_delete(db: Session, delivery_id: int) -> None:
    delivery = get_by_id(db, delivery_id)
    if delivery:
        delivery.is_active = False
        db.commit()
