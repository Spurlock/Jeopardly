from django.http import HttpResponse
from django.template import loader
from rest_framework.renderers import JSONRenderer

from .models import Category
from .serializers import CategorySerializer
from .utils import wipe_game_data, fetch_raw_categories, process_raw_categories, NUM_CATEGORIES


def index(request):
    template = loader.get_template('jeopardly/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def do_game_data_etl(request):
    wipe_game_data()
    fetch_raw_categories(request.GET.get('offset'))
    process_raw_categories()

    return HttpResponse("Success")  # todo: assert this less blindly


def get_game_data(request):
    cats = Category.objects.all().prefetch_related('clues')[0:NUM_CATEGORIES]

    serializer = CategorySerializer(cats, many=True)
    return HttpResponse(JSONRenderer().render(serializer.data))



