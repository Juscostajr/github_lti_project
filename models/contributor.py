class Contributor:
    def __init__(self, login: str, avatar_url: str, contributions: int) -> None:
        self.login: str = login
        self.avatar_url: str = avatar_url
        self.contributions: int = contributions

    def __repr__(self) -> str:
        return f"<Contributor login={self.login} contributions={self.contributions}>"
