import os
import psycopg2
# Create your views_package here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def top_purchases(request, input_match_id):
    # connection = function_connection()
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )

    cursor = connection.cursor()
    cursor.execute("""""", [input_match_id])
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


@api_view(['GET'])
def usage(request, input_ability_id):
    # connection = function_connection()
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )

    cursor = connection.cursor()
    cursor.execute("""""", [input_ability_id])
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


@api_view(['GET'])
def tower_kills(request):
    # connection = function_connection()
    connection = psycopg2.connect(
        dbname=os.getenv('NAME_DATABASE'),
        user=os.getenv('AIS_USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('DBS_IP'),
        port=os.getenv('DBS_PORT')
    )

    cursor = connection.cursor()
    cursor.execute("""""")
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})
