import requests
import logging
from urllib.parse import urlparse
from config import Config
from utils.http_client import get_json
from adapters import github_adapter

logger = logging.getLogger(__name__)


def get_all_commits(repo_url):
    owner_repo = extract_owner_repo(repo_url)
    if not owner_repo:
        return []
    api_url = f"https://api.github.com/repos/{owner_repo}/commits"
    
    json_data = get_json(
        api_url, 
        {'Authorization': f'Bearer {Config.GITHUB_TOKEN}'}
    )

    return github_adapter.adapt_commits(json_data)


def get_all_contributors(repo_url):
    owner_repo = extract_owner_repo(repo_url)
    if not owner_repo:
        return []
    api_url = f"https://api.github.com/repos/{owner_repo}/contributors"
    
    json_data = get_json(
        api_url,
        {'Authorization': f'Bearer {Config.GITHUB_TOKEN}'}
    )
    
    return github_adapter.adapt_contributors(json_data)


def extract_user_repo(github_url):
    """
    Extrai o usuário e repositório de uma URL do GitHub.
    Ex: https://github.com/usuario/repositorio -> ("usuario", "repositorio")
    """
    try:
        path_parts = urlparse(github_url).path.strip("/").split("/")
        if len(path_parts) >= 2:
            user = path_parts[0]
            repo = path_parts[1]
            if repo.endswith(".git"):
                repo = repo[:-4]
            return user, repo
    except Exception as e:
        logger.warning(f"Erro ao extrair user/repo: {e}")
    return None


def extract_owner_repo(github_url):
    """
    Extrai o caminho completo "usuario/repositorio" de uma URL GitHub.
    """
    user_repo = extract_user_repo(github_url)
    if user_repo:
        return f"{user_repo[0]}/{user_repo[1]}"
    return None


def validate_repository(github_url):
    """
    Valida se um repositório GitHub existe acessando a API pública.
    """
    user_repo = extract_user_repo(github_url)
    if not user_repo:
        return False

    user, repo = user_repo
    api_url = f"https://api.github.com/repos/{user}/{repo}"

    try:
        response = requests.get(
            api_url, 
            timeout=5, 
            headers={'Authorization': f'Bearer {Config.GITHUB_TOKEN}'}
        )
        return response.ok
    except requests.RequestException as e:
        logger.warning(f"Erro ao acessar {api_url}: {e}")
        return False
