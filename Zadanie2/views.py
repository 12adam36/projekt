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
    data_version = cursor.fetchone()
    cursor.execute("SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size;")
    data_size = cursor.fetchone()
    return JsonResponse({'pgsql': {'version': data_version[0], 'dota2_db_size': data_size[0]}})


@api_view(['GET'])
def patches(request):
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )
    cursor = connection.cursor()
    cursor.execute("select")
    return JsonResponse({"halo": 'halo'})


@api_view(['GET'])
def game_exp(request, input_player_id):
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )

    cursor = connection.cursor()
    name = 'select coalesce(players.nick,unknown ) from players where players.id = input_player_id'
    #cursor.execute("select coalesce(players.nick,unknown ) from players where players.id = input_player_id") #sem sa pise sql
    cursor.execute(name)
    nickname = cursor.fetchone()

    return JsonResponse({"halo": name})
