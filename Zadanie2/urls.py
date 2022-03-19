from django.urls import path

from . import views

urlpatterns = [
    path('v1/health/', views.index, name=''),
    path('v2/patches', views.patches, name=''),
    path('v2/players/<int:input_player_id>/game_exp', views.game_exp, name=''),
]
