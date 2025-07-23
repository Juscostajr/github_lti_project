from flask import Blueprint, request, render_template, redirect, url_for, session
from pylti.flask import lti
from sqlalchemy.orm import Session
from database import SessionLocal
from services import github_service
from domain.models import Activity, Delivery, ActivityHistory
from datetime import datetime

shared_lti = Blueprint('shared_lti', __name__)


@shared_lti.route('/launch', methods=['POST'])
@lti(request='initial', app=None)
def launch(lti):
    print(lti)
    session["user_id"] = lti.user_id
    session["resource_link_id"] = request.form.get("resource_link_id")
    return redirect(url_for("shared_lti.dashboard"))


@shared_lti.route('/link', methods=['POST'])
@lti(request='session', app=None)
def link_repository(lti):
    user_id = session.get("user_id")
    resource_link_id = session.get("resource_link_id")
    github_url = request.form.get('github_url')

    if not user_id or not resource_link_id:
        return "Invalid LTI session. Please access the activity again via Moodle.", 400

    if not github_service.validate_repository(github_url):
        return render_template("form.html", error="Invalid repository.", github_url=github_url)

    db: Session = SessionLocal()

    try:
        # Busca ou cria Activity
        activity = db.query(Activity).filter_by(id=resource_link_id, is_active=True).first()
        if not activity:
            activity = Activity(id=resource_link_id, title=f"Atividade {resource_link_id}", github_repo_url=github_url)
            db.add(activity)
        else:
            activity.github_repo_url = github_url
            activity.last_modified = datetime.utcnow()

        # Verifica se o aluno já entregou
        delivery = db.query(Delivery).filter_by(
            activity_id=activity.id,
            student_id=user_id,
            is_active=True
        ).first()

        if delivery:
            delivery.last_modified = datetime.utcnow()
        else:
            delivery = Delivery(activity=activity, student_id=user_id)
            db.add(delivery)

        # Registra histórico da alteração
        history = ActivityHistory(activity=activity)
        db.add(history)

        db.commit()
    except Exception as e:
        db.rollback()
        return f"Erro ao salvar entrega: {str(e)}", 500
    finally:
        db.close()

    return redirect(url_for("shared_lti.dashboard"))


@shared_lti.route('/dashboard')
@lti(request='session', app=None)
def dashboard(lti):
    user_id = session.get("user_id")
    resource_link_id = session.get("resource_link_id")

    if not user_id or not resource_link_id:
        return "Invalid LTI session", 400

    db: Session = SessionLocal()
    try:
        activity = db.query(Activity).filter_by(id=resource_link_id, is_active=True).first()
    finally:
        db.close()

    if activity:
        commits = github_service.get_all_commits(activity.github_repo_url)
        contributors = github_service.get_all_contributors(activity.github_repo_url)
        return render_template("dashboard.html", github_url=activity.github_repo_url, commits=commits, contributors=contributors)

    return render_template("form.html")
