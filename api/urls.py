from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, SocialMediaViewSet, CarouselImageViewSet, LogoViewSet
from .views import MenuViewSet, SubMenuViewSet, SubSubMenuViewSet, ThemeColorViewSet


# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'contact', ContactViewSet)
router.register(r'socialmedia', SocialMediaViewSet)
router.register(r'carousel', CarouselImageViewSet)
router.register(r'logo', LogoViewSet)

router.register(r'menus', MenuViewSet)
router.register(r'sub-menus', SubMenuViewSet)
router.register(r'sub-sub-menus', SubSubMenuViewSet)
router.register(r'themecolors', ThemeColorViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
