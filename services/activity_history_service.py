from sqlalchemy.orm import Session
from domain.models import ActivityHistory
from repositories import activity_history_repository

def log_activity_change(db: Session, activity_id: int) -> ActivityHistory:
    history = ActivityHistory(activity_id=activity_id)
    return activity_history_repository.create(db, history)

def list_activity_history(db: Session, activity_id: int) -> list[ActivityHistory]:
    return activity_history_repository.list_by_activity(db, activity_id)
