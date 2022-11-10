# Generated by Django 4.1.3 on 2022-11-10 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.director'),
        ),
    ]