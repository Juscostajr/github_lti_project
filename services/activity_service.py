from sqlalchemy.orm import Session
from domain.models import Activity
from repositories import activity_repository

def create_activity(db: Session, title: str, github_repo_url: str) -> Activity:
    activity = Activity(title=title, github_repo_url=github_repo_url)
    return activity_repository.create(db, activity)

def get_activity(db: Session, activity_id: int) -> Activity | None:
    return activity_repository.get_by_id(db, activity_id)

def list_activities(db: Session) -> list[Activity]:
    return activity_repository.list_all(db)

def delete_activity(db: Session, activity_id: int) -> None:
    activity_repository.soft_delete(db, activity_id)
