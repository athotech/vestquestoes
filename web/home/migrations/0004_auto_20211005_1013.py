# Generated by Django 3.2.7 on 2021-10-05 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211005_1007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='alternativas',
            new_name='Alternativa',
        ),
        migrations.RenameModel(
            old_name='Perguntas',
            new_name='Pergunta',
        ),
    ]