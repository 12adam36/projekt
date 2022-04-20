import os
import psycopg2
# Create your views_package here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . import zadanie_2


@api_view(['GET'])
def patches(request):
    cursor = zadanie_2.function_connection()
    cursor.execute("select")
    return JsonResponse({"halo": 'halo'})


@api_view(['GET'])
def game_exp(request, input_player_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""select p.id, COALESCE(p.nick, 'unknown'), m.id, h.localized_name, ROUND((m.duration::decimal)/60, 2)  as duration, (coalesce(mpd.xp_hero,0)+coalesce(mpd.xp_creep,0)+coalesce(mpd.xp_other,0)+coalesce(mpd.xp_roshan,0)) as experiences_gained, mpd.level,
       case when(mpd.player_slot >= 0 and mpd.player_slot <= 4 and m.radiant_win = true) then true
           when (mpd.player_slot >= 128 and mpd.player_slot <= 132 and m.radiant_win = false) then true
           else false
           end as win
from matches_players_details as mpd
join matches as m on mpd.match_id = m.id
join heroes as h on mpd.hero_id = h.id
join players as p on mpd.player_id = p.id
where p.id = %s
order by m.id ASC;""", [input_player_id])
    data = cursor.fetchall()
    array = []
    player_nick = ""

    for line in data:
        player_nick = line[1]

        match = {
            "match_id": line[2],
            "hero_localized_name": line[3],
            "match_duration_minutes": float(line[4]),
            "experiences_gained": line[5],
            "level_gained": line[6],
            "winner": line[7],
        }
        array.append(match)

    return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})


@api_view(['GET'])
def game_objectives(request, input_player_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""select p.id, coalesce(p.nick,'unknown'), h.localized_name, mpd.match_id, (select distinct coalesce(g_o.subtype,'NO_ACTION')),
       coalesce(NULLIF(count(g_o.subtype),0),1)
from matches_players_details as mpd
join players as p on mpd.player_id = p.id
join heroes as h on mpd.hero_id = h.id
left outer join game_objectives as g_o on mpd.id = g_o.match_player_detail_id_1
where p.id = %s group by p.id, mpd.match_id, h.localized_name, g_o.subtype, g_o.match_player_detail_id_1
order by mpd.match_id ASC;""", [input_player_id])
    data = cursor.fetchall()
    array_2 = []
    player_nick = ""
    x = 0
    for line in data:
        player_nick = line[1]
        array = []
        m_id = line[3]
        if x == 0 or (x != 0 and data[x - 1][3] != m_id):
            for line2 in data:
                if line2[3] == m_id:
                    action = {
                        "hero_action": line2[4],
                        "count": line2[5],
                    }
                    array.append(action)
            match = {
                "match_id": line[3],
                "hero_localized_name": line[2],
                "actions": array,
            }
            array_2.append(match)
        x = x + 1

    return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array_2})


@api_view(['GET'])
def abilities(request, input_player_id):
    cursor = zadanie_2.function_connection()
    cursor.execute("""""", [input_player_id])
    data = cursor.fetchall()

    #return JsonResponse({"id": input_player_id, "player_nick": player_nick, "matches": array})
