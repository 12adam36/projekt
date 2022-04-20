import os
import psycopg2
# Create your views_package here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . import zadanie_2


# endpoint 1
@api_view(['GET'])
def top_purchases(request, input_match_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""
    select * from(
        select *, row_number() over (partition by hero_id) as k from (
            select distinct mpd.hero_id, h.localized_name, pl.item_id, i.name, count(pl.item_id) as pc, mpd.player_slot
            from matches_players_details as mpd
            join heroes as h on mpd.hero_id = h.id
            join matches as m on m.id = mpd.match_id
            join purchase_logs pl on mpd.id = pl.match_player_detail_id
            join items as i on pl.item_id = i.id
            where mpd.match_id = %s and ((m.radiant_win is true and mpd.player_slot between 0 and 4) or (m.radiant_win is false and mpd.player_slot between 128 and 132))
            group by pl.item_id, i.name, mpd.player_slot, mpd.hero_id, h.localized_name
            order by mpd.hero_id asc, pc desc, i.name asc) as jump
        group by item_id, name, player_slot, hero_id, localized_name, jump.pc
        order by hero_id asc, pc desc, name asc) as rank
    where k < 6
    group by item_id, name, player_slot, hero_id, localized_name, rank.k, rank.pc
    order by hero_id asc, pc desc, name asc;""", [input_match_id])
    data = cursor.fetchall()
    heroes = []
    purchases = []
    check = 1
    for line in data:
        purchases_2 = {
            "id": line[2],
            "name": line[3],
            "count": line[4],
        }
        purchases.append(purchases_2)
        if check == 5:
            check = 0
            heroe_2 = {
                "id": line[0],
                "name": line[1],
                "top_purchases": purchases,
            }
            heroes.append(heroe_2)
            purchases = []
        check += 1
    return JsonResponse({"id": input_match_id, "heroes": heroes})


# endpoint 2
@api_view(['GET'])
def usage(request, input_ability_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""""", [input_ability_id])
    data = cursor.fetchall()

    # return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


# endpoint 3
@api_view(['GET'])
def tower_kills(request):
    cursor = zadanie_2.function_connection()
    cursor.execute("""with Streaks as(
select heroes.localized_name, game_objectives.time, row_number() over (partition by match_id order by game_objectives.time) as Act1,
       row_number() over (partition by heroes.localized_name order by game_objectives.time) as Act2,
       (row_number() over (order by game_objectives.time) - row_number() over (partition by heroes.localized_name order by game_objectives.time))Difference
    from game_objectives
    join matches_players_details mpd
on game_objectives.match_player_detail_id_1 = mpd.id
    join matches
on mpd.match_id = matches.id
    join heroes
on mpd.hero_id = heroes.id
    Where game_objectives.subtype = 'CHAT_MESSAGE_TOWER_KILL'
    group by duration, heroes.localized_name,game_objectives.subtype, matches.id, game_objectives.time, match_id
    order by matches.id ASC, game_objectives.time deSC)
select *, row_number() over (partition by Difference order by time) Streaks from Streaks
order by time;""")
    data = cursor.fetchall()
    array = []
    for line in data:
        element = {
            "id": line[0],
            "name": line[1],
            "tower_kills": line[2],
        }
        array.append(element)

    return JsonResponse({"heroes": array})
