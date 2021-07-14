# Generated by Django 3.2.5 on 2021-07-11 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardly', '0002_auto_20210711_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='rawcategory',
            options={'verbose_name_plural': 'RawCategories'},
        ),
        migrations.RenameField(
            model_name='rawcategory',
            old_name='clues_json',
            new_name='json',
        ),
        migrations.RemoveField(
            model_name='rawcategory',
            name='clues_count',
        ),
    ]
