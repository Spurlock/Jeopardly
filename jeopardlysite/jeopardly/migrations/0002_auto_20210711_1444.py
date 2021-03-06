# Generated by Django 3.2.5 on 2021-07-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('clues_count', models.IntegerField(default=0)),
                ('clues_json', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='clue',
            old_name='votes',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='category',
            name='clues_count',
        ),
    ]
