from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Clue(models.Model):
    solution = models.CharField(max_length=200)
    prompt = models.CharField(max_length=1000)
    value = models.IntegerField(null=True)
    category = models.ForeignKey(Category, related_name='clues', db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%d: %s for %d" % (self.id, self.category.title, self.value or 0)


class RawCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    json = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "RawCategories"
