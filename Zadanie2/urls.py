from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('patches/', views.patches, name=''),
    path('players/<int:input_player_id>/game_exp/', views.game_exp, name=''),
    path('players/<int:input_player_id>/game_objectives/', views.game_objectives, name=''),
    path('players/<int:input_player_id>/abilities/', views.abilities, name=''),
]
