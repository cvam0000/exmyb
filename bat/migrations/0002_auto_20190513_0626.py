# Generated by Django 2.2 on 2019-05-13 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bat',
            name='answer',
        ),
        migrations.CreateModel(
            name='Ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('user', models.CharField(max_length=300)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bat.Bat')),
            ],
        ),
    ]
