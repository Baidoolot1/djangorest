# Generated by Django 4.1.2 on 2022-11-04 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_review_review_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default='5', max_length=1),
        ),
    ]
