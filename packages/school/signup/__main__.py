from database import PyMongo
from jwtHelper import ApiJWTAuthentication
import json
from passlib.hash import bcrypt
def main(request_data):
    try:
        username=request_data['email']
        password=request_data['password']
        password=bcrypt.hash(password)
        refresh_token=ApiJWTAuthentication.getRefreshToken(username)
        refresh_token=refresh_token['refresh_token']
        userseq=PyMongo.getData('counter','table','user')[0]
        userseq=userseq['counter']
        user = {"user_id": userseq, "password": password, "email": request_data['email'], "refresh_token":refresh_token,"user_type":0,"firebase_token":""}
        PyMongo.insertData('user',user)
        userseq=userseq+1

        schoolseq=PyMongo.getData('counter','table','school')[0]['counter']
        school={"school_id": schoolseq, "name": request_data['name'], "email": request_data['email'], "address":request_data['address'],"city":request_data['city'],'country':request_data['country'],'state':request_data['state'],'phone':request_data['phone'],'mobile':request_data['mobile']}
        PyMongo.insertData('school',school)
        schoolseq=schoolseq+1
        ##User Org table add
        PyMongo.insertData("user_org",{"user_id":userseq,"org_id":schoolseq})

        PyMongo.updateData("counter", "counter", userseq, "table", "user")
        PyMongo.updateData("counter", "counter", schoolseq, "table", "school")
        access_token=ApiJWTAuthentication.getAccessToken(refresh_token)['access_token']
        response={"message":"Registered successfully","access_token":access_token,"refresh_token":refresh_token,"success":True,"user_type":0}
        return {"body":{
                "success":(True),
                "message":"Registered successfully",
                "access_token":(access_token),
                "refresh_token":(refresh_token),
                "user_type":0,
                "statusCode":200
            }}

    except Exception as e:
        return {"body":{
            "statusCode": 400,
            "message":str(e),
            "success":(False)
        }}

