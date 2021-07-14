from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('etl', views.do_game_data_etl, name='etl'),
    path('game-data', views.get_game_data, name='game_data')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
