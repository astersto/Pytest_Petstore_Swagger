import os
from dotenv import load_dotenv

load_dotenv()

BASE_URI = os.getenv("BASE_URI")
TIMEOUT = int(os.getenv("TIMEOUT", 30))

HEADERS ={
    "Content-Type" : os.getenv("CONTENT_TYPE")
}
