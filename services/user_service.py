from base.base_test import BaseTest
from constants.endpoints import (
CREATE_USER, LOGOUT_USER, LOGIN_USER, GET_USER, UPDATE_USER, DELETE_USER
)

class UserService(BaseTest):

    def create_user(self,body):
        return self.post(CREATE_USER, body)

    def login_user(self, username, password):
        return self.get(LOGIN_USER, params={"username" : username, "password" : password})

    def logout_user(self):
        return self.get(LOGOUT_USER)

    def get_user(self, username):
        return self.get(GET_USER.format(username=username))

    def update_user(self, username, body):
        return self.put(UPDATE_USER.format(username=username), body)

    def delete_user(self, username):
        return self.delete(DELETE_USER.format(username=username))
