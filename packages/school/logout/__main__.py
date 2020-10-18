from database import PyMongo
from jwtHelper import ApiJWTAuthentication
import json
from passlib.hash import bcrypt
def main(request_data):
    try:
        PyMongo.updateData('user','refresh_token','','email',request_data['email'])
        return {"body":{
            "statusCode": 200,
            "message": "logged out successfully",
            "success": (True)
        }}
    except Exception as e:
        return {"body":{
            "statusCode": 400,
            "message": str(e),
            "success": (False)
        }}
