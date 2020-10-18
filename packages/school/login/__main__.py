from database import PyMongo
from jwtHelper import ApiJWTAuthentication
import json
from passlib.hash import bcrypt
def main(request_data):
    try:
        username=request_data['email']
        password=request_data['password']
        user_record=PyMongo.getData('user','email',username)

        password_fromDB=user_record[0]['password']
        if bcrypt.verify(password, password_fromDB):
            refresh_token=ApiJWTAuthentication.getRefreshToken(username)['refresh_token']
            PyMongo.updateData('user','refresh_token',refresh_token,'email',username)
            access_token = ApiJWTAuthentication.getAccessToken(refresh_token)['access_token']
            user_type = user_record[0]['user_type']
            return {"body":{
                "message": "Login successful",
                "status_code": 200,
                "success": (True),
                "access_token":(access_token),
                "refresh_token":(refresh_token),
                "user_type":(user_type)
            }}
        else:
            return {"body":{
                "message": "Invalid password",
                "status_code": 200,
                "success": (False)
            }}
    except Exception as e:
        return {"body":{
            "statusCode": 400,
            "message": str(e),
            "success": (False)
        }}

