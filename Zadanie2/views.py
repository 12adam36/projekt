import os
import psycopg2
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    data_version = cursor.fetchall()
    cursor.execute("SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size;")
    data_size = cursor.fetchall()
    return JsonResponse({"pgsql": {"version": data_version[0], "dota2_db_size": data_size[0]}})
