# Generated by Django 5.0.4 on 2024-09-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_menu_sub_menus_remove_submenu_sub_sub_menus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=50, unique=True)),
                ('color_code', models.CharField(max_length=50)),
            ],
        ),
    ]
