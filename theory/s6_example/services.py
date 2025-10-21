from .utils import format_data

class DataService:
    @staticmethod
    def fetch_user_data(username):
        # Simulate fetching data
        data = {username: "some data"}
        return format_data(data)

    @staticmethod
    def create_user(username):
        return User(username)

