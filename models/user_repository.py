class UserRepository:
    def __init__(self, user: str, repository: str) -> None:
        self.user: str = user
        self.repository: str = repository

    def __repr__(self) -> str:
        return f"<UserRepository user={self.user} repository={self.repository}>"
