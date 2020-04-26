# Generated by Django 3.0.3 on 2020-04-24 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BuctLib', '0004_auto_20200424_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Time', models.DateTimeField()),
                ('Content', models.TextField()),
                ('ReadTimes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='消息标题')),
                ('Content', models.TextField()),
                ('MTime', models.DateTimeField()),
                ('Status', models.CharField(default='未读', max_length=20)),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BuctLib.Reader')),
            ],
        ),
    ]