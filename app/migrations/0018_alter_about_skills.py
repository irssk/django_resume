# Generated by Django 4.2.3 on 2023-08-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='skills',
            field=models.ManyToManyField(to='app.skill'),
        ),
    ]