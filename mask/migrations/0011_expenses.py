# Generated by Django 5.2.1 on 2025-06-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0010_alter_expense_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
