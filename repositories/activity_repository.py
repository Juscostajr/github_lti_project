from sqlalchemy.orm import Session
from domain.models import Activity

def get_by_id(db: Session, activity_id: int) -> Activity | None:
    return db.query(Activity).filter(Activity.id == activity_id, Activity.is_active == True).first()

def create(db: Session, activity: Activity) -> Activity:
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

def list_all(db: Session) -> list[Activity]:
    return db.query(Activity).filter(Activity.is_active == True).all()

def soft_delete(db: Session, activity_id: int) -> None:
    activity = get_by_id(db, activity_id)
    if activity:
        activity.is_active = False
        db.commit()