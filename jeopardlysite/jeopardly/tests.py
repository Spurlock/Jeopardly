from django.test import TestCase, Client
from django.urls import reverse
import json

from .models import Category, Clue
from .utils import NUM_CATEGORIES


class CategoryTestCase(TestCase):
    def setUp(self):
        colors_cat = Category.objects.create(title="Colors")
        shapes_cat = Category.objects.create(title="Shapes")

        # create too many categories, to later test that we don't load them all
        for i in range(10):
            Category.objects.create(title="Empty %d" % i)

        Clue.objects.create(solution="Red", prompt="Brick", value=100, category=colors_cat)
        Clue.objects.create(solution="Green", prompt="Lime", value=200, category=colors_cat)
        Clue.objects.create(solution="Blue", prompt="Sky", value=300, category=colors_cat)

        Clue.objects.create(solution="Triangle", prompt="Three Sides", value=100, category=shapes_cat)
        Clue.objects.create(solution="Pentagon", prompt="Five Sides", value=200, category=shapes_cat)

    def test_correct_clue_categories(self):
        # test relationships between models

        colors_cat = Category.objects.filter(clues__prompt="Brick")[0]
        self.assertEqual(colors_cat.title, "Colors")

        colors_clue = Clue.objects.filter(prompt="Lime")[0]
        self.assertEqual(colors_clue.category.title, "Colors")

        shapes_cat = Category.objects.filter(title="Shapes").prefetch_related('clues')[0]
        self.assertEqual(shapes_cat.clues.get(value=100).solution, "Triangle")

    def test_game_load(self):
        client = Client()

        # does the request succeed?
        response = client.get(reverse('game_data'))
        self.assertEqual(response.status_code, 200)

        # do we load the correct number of categories?
        content = json.loads(response.content)
        self.assertEqual(len(content), NUM_CATEGORIES)

        # does at least one category have actual clues?
        clueful_cat = None
        for cat in content:
            if cat['clues']:
                clueful_cat = cat
                break
        self.assertIsNotNone(clueful_cat)
        self.assertIsInstance(clueful_cat['clues'][0]['prompt'], str)

    def test_db_hits(self):
        client = Client()

        with self.assertNumQueries(2):
            response = client.get(reverse('game_data'))


class EtlTestCase(TestCase):
    def setUp(self):
        client = Client()
        response = client.get(reverse('etl'), {'offset': 5})

    def test_etl_offset(self):
        truman_cats = Category.objects.filter(title="harry truman")
        self.assertEqual(len(truman_cats), 1)
