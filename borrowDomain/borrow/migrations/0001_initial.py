# Generated by Django 2.2.4 on 2019-08-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prestamista', models.IntegerField()),
                ('id_solicitante', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
            ],
        ),
    ]
