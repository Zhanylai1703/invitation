# Generated by Django 5.1 on 2024-08-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_invitation_wish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wish', models.TextField()),
            ],
        ),
    ]
