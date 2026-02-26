import requests
from config.config_reader import BASE_URI,HEADERS,TIMEOUT

class BaseTest:

    def get(self, endpoint, params=None):
        return requests.get(BASE_URI + endpoint, headers= HEADERS, params=params, timeout=TIMEOUT)

    def post(self, endpoint, body=None):
        return requests.post(BASE_URI + endpoint, headers=HEADERS, json=body, timeout=TIMEOUT)

    def put(self, endpoint, body=None):
        return requests.put(BASE_URI + endpoint, headers=HEADERS, json=body, timeout=TIMEOUT)

    def delete(self, endpoint, params=None):
        return requests.delete(BASE_URI + endpoint, headers=HEADERS, params=params, timeout=TIMEOUT)