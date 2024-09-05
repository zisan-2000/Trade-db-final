from rest_framework import viewsets
from .models import Contact, SocialMedia, CarouselImage, Logo
from .serializers import ContactSerializer, SocialMediaSerializer, CarouselImageSerializer, LogoSerializer

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class CarouselImageViewSet(viewsets.ModelViewSet):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer

#menu views

#menu views

from rest_framework import viewsets
from .models import Menu, SubMenu, SubSubMenu
from .serializers import MenuSerializer, SubMenuSerializer, SubSubMenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer

class SubSubMenuViewSet(viewsets.ModelViewSet):
    queryset = SubSubMenu.objects.all()
    serializer_class = SubSubMenuSerializer


from rest_framework import viewsets
from .models import ThemeColor
from .serializers import ThemeColorSerializer

class ThemeColorViewSet(viewsets.ModelViewSet):
    queryset = ThemeColor.objects.all()
    serializer_class = ThemeColorSerializer
