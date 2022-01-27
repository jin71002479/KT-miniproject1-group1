# Generated by Django 2.2.5 on 2022-01-27 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freewrite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_subject', models.CharField(max_length=200)),
                ('free_content', models.TextField()),
                ('free_pub_date', models.DateTimeField()),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_create_date', models.DateTimeField()),
                ('freewrite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeboard.Freewrite')),
            ],
        ),
    ]
