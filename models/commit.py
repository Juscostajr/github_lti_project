from datetime import datetime

class Commit:
    def __init__(self, message: str, date: datetime, author: str):
        self.message = message
        self.date = datetime.fromisoformat(date.replace('Z', '+00:00'))
        self.author = author

    def __repr__(self):
        return f"<Commit author={self.author} date={self.date} message={self.message[:30]}>"

    def get_ptbr_date(self) -> str:
        return self.date.strftime('%d/%m/%Y %H:%M')
