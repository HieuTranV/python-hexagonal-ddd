from .entities import User
class UserAggregate:
    def __init__(self, user: User):
        self.user = user