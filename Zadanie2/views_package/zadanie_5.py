import os
import psycopg2
# Create your views_package here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . import zadanie_2


@api_view(['GET'])
def top_purchases(request, input_match_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""""", [input_match_id])
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


@api_view(['GET'])
def usage(request, input_ability_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""""", [input_ability_id])
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


@api_view(['GET'])
def tower_kills(request):
    cursor = zadanie_2.function_connection()
    cursor.execute("""""")
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})
