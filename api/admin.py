from django.contrib import admin
from .models import Menu, SubMenu, SubSubMenu, ThemeColor

admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(SubSubMenu)

# You can add initial data via the shell or a data migration


# ThemeColor.objects.create(page_name="homepage", color_code="bg-red-500")
# ThemeColor.objects.create(page_name="about", color_code="bg-blue-500")
# ThemeColor.objects.create(page_name="clients", color_code="bg-green-500")
# ThemeColor.objects.create(page_name="contacts", color_code="bg-slate-500")
# ThemeColor.objects.create(page_name="maintenance", color_code="bg-orange-500")
# ThemeColor.objects.create(page_name="media", color_code="bg-purple-500")
# ThemeColor.objects.create(page_name="partners", color_code="bg-teal-500")
# ThemeColor.objects.create(page_name="solutions", color_code="bg-yellow-500")
