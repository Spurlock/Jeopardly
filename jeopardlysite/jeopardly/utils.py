from random import randint
import requests
import json
from .models import RawCategory, Category, Clue


NUM_CATEGORIES = 6  # the number of categories in a game
MAX_OFFSET = 2000  # empirically, it is safe to offset the category fetch by at least this much


def fetch_raw_categories(offset=None):
    """retrieve categories (with clues) from the API, store in raw form"""

    # offset functions as a seed for the game. randomize if not provided.
    if offset is None:
        offset = randint(0, MAX_OFFSET)

    # fetch category overviews from API
    cat_request_params = {
        'count': NUM_CATEGORIES,
        'offset': offset
    }
    categories_resp = requests.get("http://jservice.io/api/categories", params=cat_request_params)
    categories = categories_resp.json()

    # fetch complete objects (including clues) for each category, then save in raw form
    raw_cats = []
    for cat in categories:
        cat_detail_resp = requests.get("http://jservice.io/api/category", params={'id': cat['id']})

        raw_cat = RawCategory(
            id=cat['id'],
            title=cat['title'],
            json=cat_detail_resp.text
        )
        raw_cats.append(raw_cat)
    RawCategory.objects.bulk_create(raw_cats)


def process_raw_categories():
    """transform raw categories into processed categories and clues, then save those"""

    all_raw_cats = RawCategory.objects.all()
    final_cats = []
    final_clues = []

    for raw_cat in all_raw_cats:
        cat = Category(id=raw_cat.id, title=raw_cat.title)
        final_cats.append(cat)

        parsed_cat = json.loads(raw_cat.json)
        for raw_clue in parsed_cat['clues']:
            clue = Clue(
                solution=raw_clue['answer'],
                prompt=raw_clue['question'],
                value=raw_clue['value'],
                category=cat
            )
            final_clues.append(clue)

    Category.objects.bulk_create(final_cats)
    Clue.objects.bulk_create(final_clues)


def wipe_game_data():
    """clear out all db objects"""

    RawCategory.objects.all().delete()
    Category.objects.all().delete()
    Clue.objects.all().delete()