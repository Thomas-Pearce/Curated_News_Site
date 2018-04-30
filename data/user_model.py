from data import DBClient
import datetime

"""Users have the following format in the DB

{'_id': "MongoDB id as a mongo objectID object", 
'name': "The users chosen name as a string"
'email': "The users email as a string"
'password': "The users password, stored in an MD5 hash as a string"}
"""


