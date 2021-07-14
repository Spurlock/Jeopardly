from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Clue


class CategorySerializer(ModelSerializer):

    clues = SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'title',
            'clues'
        ]

    def get_clues(self, instance):
        return ClueSerializer(instance.clues, many=True).data


class ClueSerializer(ModelSerializer):
    class Meta:
        model = Clue
        fields = [
            'solution',
            'prompt',
            'value',
            'category'
        ]
