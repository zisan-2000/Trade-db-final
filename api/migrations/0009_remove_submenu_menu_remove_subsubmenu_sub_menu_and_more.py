# Generated by Django 5.0.4 on 2024-09-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_menu_sub_menu_remove_submenu_sub_sub_menu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='subsubmenu',
            name='sub_menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='sub_menus',
            field=models.ManyToManyField(blank=True, related_name='menus', to='api.submenu'),
        ),
        migrations.AddField(
            model_name='submenu',
            name='sub_sub_menus',
            field=models.ManyToManyField(blank=True, related_name='sub_menus', to='api.subsubmenu'),
        ),
    ]
