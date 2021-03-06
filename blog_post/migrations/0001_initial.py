# Generated by Django 3.1.3 on 2020-11-26 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_by', models.CharField(blank=True, max_length=80, null=True)),
                ('body', models.TextField()),
                ('like_status', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('no response', 'no response')], default='no response', max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_post.post')),
            ],
        ),
    ]
