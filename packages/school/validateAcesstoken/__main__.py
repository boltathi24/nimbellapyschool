from database import PyMongo
from jwtHelper import ApiJWTAuthentication
import json
from passlib.hash import bcrypt
def main(request_data):
    try:
        response=ApiJWTAuthentication.validateAccessToken(request_data['access_token'])
        return {"body":response}
    except Exception as e:
        return {"body":{"message":str(e),"success":(False),"statusCode":400}}

