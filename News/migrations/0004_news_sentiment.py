# Generated by Django 5.0.2 on 2024-02-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_news_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='sentiment',
            field=models.CharField(default='neutral', max_length=20),
            preserve_default=False,
        ),
    ]
