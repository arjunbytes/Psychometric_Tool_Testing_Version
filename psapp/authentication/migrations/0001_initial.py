# Generated by Django 5.0.6 on 2024-05-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.IntegerField()),
                ('question2', models.IntegerField()),
                ('question3', models.IntegerField()),
                ('question4', models.IntegerField()),
                ('question5', models.IntegerField()),
                ('question6', models.IntegerField()),
                ('question7', models.IntegerField()),
                ('question8', models.IntegerField()),
                ('question9', models.IntegerField()),
                ('question10', models.IntegerField()),
            ],
        ),
    ]
