import requests
from typing import List, Optional
from config import Config
from models.commit import Commit
from models.contributor import Contributor
from models.user_repository import UserRepository

def get_user_repository(github_url: str) -> Optional[UserRepository]:
    try:
        url = github_url.rstrip('/')
        if url.endswith('.git'):
            url = url[:-4]
        parts = url.split('/')
        user = parts[-2]
        repo = parts[-1]
        return UserRepository(user, repo)
    except Exception:
        return None

def get_all_commits(github_url: str, max_commits=50, token=None) -> List[Commit]:
    user_repo = get_user_repository(github_url)
    if not user_repo:
        return []
    user = user_repo.user
    repo = user_repo.repository

    api_url = f'https://api.github.com/repos/{user}/{repo}/commits'
    if token is None:
        token = Config.GITHUB_TOKEN
    headers: dict = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    try:
        res = requests.get(api_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            return [
                Commit(
                    message=c['commit']['message'],
                    date=c['commit']['committer']['date'],
                    author=c['commit']['author']['name']
                ) for c in data[:max_commits]
            ]
    except Exception:
        pass
    return []

def get_all_contributors(github_url: str, token=None) -> List[Contributor]:
    user_repo = get_user_repository(github_url)
    if not user_repo:
        return []
    user = user_repo.user
    repo = user_repo.repository

    api_url = f'https://api.github.com/repos/{user}/{repo}/contributors'
    if token is None:
        token = Config.GITHUB_TOKEN
    headers: dict = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    try:
        res = requests.get(api_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            return [
                Contributor(
                    login=c['login'],
                    avatar_url=c['avatar_url'],
                    contributions=c['contributions']
                ) for c in data
            ]
    except Exception:
        pass
    return []

def validate_repository(url: str) -> bool:
    try:
        user_repo = get_user_repository(url)
        if not user_repo:
            return False
        user = user_repo.user
        repo = user_repo.repository
        api_url = f'https://api.github.com/repos/{user}/{repo}'
        res = requests.get(api_url)
        if res.status_code == 200:
            return True
    except Exception:
        pass
    return False