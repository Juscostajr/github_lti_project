from sqlalchemy.orm import Session
from domain.models import ActivityHistory

def create(db: Session, history: ActivityHistory) -> ActivityHistory:
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

def list_by_activity(db: Session, activity_id: int) -> list[ActivityHistory]:
    return db.query(ActivityHistory).filter(ActivityHistory.activity_id == activity_id, ActivityHistory.is_active == True).all()
