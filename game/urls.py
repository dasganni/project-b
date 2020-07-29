from django.urls import path, include
from . import views


app_name = "game"

extra_patterns = [
    path("map/", include('maptool.urls')),
]


urlpatterns = [
    path("games-list/", views.listGames.as_view(), name="games_list"),
    path("create-game/", views.createGame.as_view(), name="create_game"),
    path("update-game/<int:game_id>/", views.updateGame.as_view(), name="update_game"),
    path("delete-game/<int:game_id>/", views.deleteGame.as_view(), name="delete_game"),
    path("<int:game_id>/", include(extra_patterns)),
]
