# Generated by Django 2.2 on 2020-08-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tweet', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flag', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuthUser')),
            ],
            options={
                'db_table': 'tweet',
            },
        ),
        migrations.CreateModel(
            name='TweetLike',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flag', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuthUser')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tweet')),
            ],
            options={
                'db_table': 'tweet_like',
            },
        ),
        migrations.CreateModel(
            name='TweetComment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flag', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuthUser')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tweet')),
            ],
            options={
                'db_table': 'tweet_comment',
            },
        ),
    ]
