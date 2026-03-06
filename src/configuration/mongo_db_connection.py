import os
import sys
import pymongo
import certifi
import pandas as pd
from typing import Optional

from src.exception import MyException

from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB

ca =certifi.where()

class MongoDBClient:
  """
  MongoDBClient is responsible for to the MongoDB database.

  Attributes:
  -------------------

  client : MongoClient
      A shared MongoClient instance for the class.
  database: Database
      A spcific database instance that MongoDBClient connects to.
  
  Methods:
  -------------------

  __init___(database_name:str) -> None
       Initializes the MongoDB connection using the given database name.
  """

  client = None 

  def __init__(self,database_name: str = DATABASE_NAME) -> None:
    """
    Initializes a connection to the MongoDB database.If no existing connection is found,it establishes a new one.
    """
    
    try:
      if MongoDBClient.client is None:
        mongo_db_url = os.getenv(MONGODB_URL_KEY)
        if mongo_db_url is None:
          raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
      
      MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
      
      self.client = MongoDBClient.client
      self.database = self.client[database_name]
      self.database_name = database_name
      logging.info("MongoDB connection successful.")
    
    except Exception as e:
      raise MyException(e,sys)
      
      

        

  

