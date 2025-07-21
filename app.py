from flask import Flask, request, render_template, redirect, url_for, session
from pylti.flask import lti
import services.github_service as github_service
import services.database_service as database_service
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/launch', methods=['POST'])
@lti(request='initial', app=app)
def launch(lti):
    user_id = lti.user_id
    resource_link_id = request.form.get("resource_link_id")
    session["user_id"] = user_id
    session["resource_link_id"] = resource_link_id
    return redirect(url_for("dashboard"))

@app.route('/link', methods=['POST'])
@lti(request='session', app=app)
def link_repository(lti):
    user_id = session.get("user_id")
    resource_link_id = session.get("resource_link_id")
    if not user_id or not resource_link_id:
        return "Invalid LTI session. Please access the activity again via Moodle.", 400
    github_url = request.form.get('github_url')
    if github_service.validate_repository(github_url):
        database_service.save_github_link(user_id, resource_link_id, github_url)
        return redirect(url_for('dashboard'))
    return render_template('form.html', error='Invalid repository.', github_url=github_url)

@app.route('/dashboard')
@lti(request='session', app=app)
def dashboard(lti):
    user_id = session.get("user_id")
    resource_link_id = session.get("resource_link_id")
    if not user_id or not resource_link_id:
        return "Invalid LTI session", 400
    github_link = database_service.get_github_link(user_id, resource_link_id)
    if github_link:
        commits = github_service.get_all_commits(github_link[0])
        contributors = github_service.get_all_contributors(github_link[0])
        return render_template("dashboard.html", github_url=github_link[0], commits=commits, contributors=contributors)
    return render_template("form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)