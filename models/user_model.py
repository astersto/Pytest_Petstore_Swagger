from dataclasses import dataclass

@dataclass
class User:
    id: int = 0
    username: str = ""
    firstName: str = ""
    lastName: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    userStatus: int = 0

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }