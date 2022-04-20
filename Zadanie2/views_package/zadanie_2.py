import os
import psycopg2
# Create your views_package here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


# funkcia na pripojenie na server
def function_connection():
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )
    connect = connection.cursor()
    return connect


@api_view(['GET'])
def index(request):
    cursor = function_connection()
    cursor.execute("SELECT VERSION()")
    data_version = cursor.fetchone()
    cursor.execute("SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size;")
    data_size = cursor.fetchone()
    return JsonResponse({'pgsql': {'version': data_version[0], 'dota2_db_size': data_size[0]}})
