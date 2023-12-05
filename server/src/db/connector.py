import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

mongo_db_user = os.getenv("MONGO_DB_USER")
mongo_db_pwd = os.getenv("MONGO_DB_PWD")

uri = f"mongodb+srv://{mongo_db_user}:{mongo_db_pwd}@mymongocluster.bcwctyv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
