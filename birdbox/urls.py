from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from birdboxapi.views import register_user, login_user, BirdView, LocationView, SightingView, WatcherView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'birds', BirdView, 'birds')
router.register(r'locations', LocationView, 'locations')
router.register(r'sightings', SightingView, 'sightings')
router.register(r'watcher', WatcherView, 'Profile')
router.register(r'watcher', WatcherView, 'Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]
