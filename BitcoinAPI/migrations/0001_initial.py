# Generated by Django 4.1.1 on 2022-09-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Bitcoin', max_length=100)),
                ('price', models.DecimalField(decimal_places=6, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
