from django.shortcuts import render
import pymysql
from sqlalchemy import create_engine
from django.http import JsonResponse
import json

# Create your views here.
def test_db(req):
    req=json.loads(req.body)
    uname=req["username"]
    conn=pymysql.connect(host="localhost", port=3306, user="root", password="00000000", database="test")
    cursor=conn.cursor()
    sql="select * from demo where name like '%{}%'"
    cursor.execute(sql.format(uname))
    result=[{"id": item[0], "name": item[1], "age": item[2]} for item in cursor.fetchall()]
    print(result)
    '''
    'Alice' result:
    ((1, 'Alice', 28), (4, 'Alice', 10))
    '''
    cursor.close()
    conn.close()
    return JsonResponse({"result":result})


def test_post(req):
    req=json.loads(req.body)
    print("content 1: "+req["key1"])
    print("content 2: "+req["key2"])
    return JsonResponse({"result": "post success"})

def test_get(req):
    req_content_1=req.GET.get("key1")
    req_content_2=req.GET.get("key2")
    print("content 1: "+req_content_1)
    print("content 2: "+req_content_2)
    return JsonResponse({"result": "get success"})