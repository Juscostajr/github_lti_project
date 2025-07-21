from datetime import datetime

class GithubLink:
    def __init__(self, user_id: str, resource_link_id: str, github_url: str, data_envio: str, ultima_alteracao: str):
        self.user_id: str = user_id
        self.resource_link_id: str = resource_link_id
        self.github_url: str = github_url
        self.data_envio: str = data_envio
        self.ultima_alteracao: str = ultima_alteracao

    def __repr__(self) -> str:
        return (f"<GithubLink user_id={self.user_id} resource_link_id={self.resource_link_id} "
                f"github_url={self.github_url} data_envio={self.data_envio} ultima_alteracao={self.ultima_alteracao}>")
