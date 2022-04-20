from django.urls import path

from .views_package import zadanie_5
from .views_package import zadanie_3
from .views_package import zadanie_2

urlpatterns = [
    path('', zadanie_2.index, name=''),
    path('patches/', zadanie_3.patches, name=''),
    path('players/<int:input_player_id>/game_exp/', zadanie_3.game_exp, name=''),
    path('players/<int:input_player_id>/game_objectives/', zadanie_3.game_objectives, name=''),
    path('players/<int:input_player_id>/abilities/', zadanie_3.abilities, name=''),
    path('matches/<int:input_match_id>/top_purchases/', zadanie_5.top_purchases, name=''),
    path('abilities/<int:input_ability_id>/usage/', zadanie_5.usage, name=''),
    path('statistics/tower_kills/', zadanie_5.tower_kills, name=''),
]
