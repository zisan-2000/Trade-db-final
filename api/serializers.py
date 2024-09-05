from rest_framework import serializers
from .models import Contact, SocialMedia, CarouselImage, Logo, ThemeColor

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['image', 'alt_text']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone', 'email']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['name', 'url', 'icon']

class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['image', 'caption']

# serializers for menu

# serializers for menu

from rest_framework import serializers
from .models import Menu, SubMenu, SubSubMenu

class SubSubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubMenu
        fields = '__all__'

class SubMenuSerializer(serializers.ModelSerializer):
    sub_sub_menu = SubSubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = SubMenu
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    sub_menu = SubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'

class ThemeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeColor
        fields = '__all__'