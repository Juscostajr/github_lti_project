from domain.models import Commit, Contributor
from datetime import datetime

def adapt_commits(data):
    return [
        Commit(
            sha=item["sha"],
            author=item["commit"]["author"]["name"],
            message=item["commit"]["message"],
            date=datetime.strptime(item["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
        ) for item in data
    ]

def adapt_contributors(data):
    return [
        Contributor(
            login=item["login"],
            avatar_url=item["avatar_url"],
            contributions=item["contributions"]
        ) for item in data
    ]
