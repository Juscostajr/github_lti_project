from sqlalchemy.orm import Session
from domain.models import Delivery
from repositories import delivery_repository

def create_delivery(db: Session, activity_id: int, studant_id: int) -> Delivery:
    delivery = Delivery(activity_id=activity_id, studant_id=studant_id)
    return delivery_repository.create(db, delivery)

def get_delivery(db: Session, delivery_id: int) -> Delivery | None:
    return delivery_repository.get_by_id(db, delivery_id)

def list_deliveries_for_activity(db: Session, activity_id: int) -> list[Delivery]:
    return delivery_repository.list_by_activity(db, activity_id)

def delete_delivery(db: Session, delivery_id: int) -> None:
    delivery_repository.soft_delete(db, delivery_id)
