from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from birdboxapi.views import Profile, register_user, login_user, BirdView, LocationView, SightingView, get_watcher_profile


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'birds', BirdView, 'birds')
router.register(r'locations', LocationView, 'locations')
router.register(r'sightings', SightingView, 'sightings')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    # path('birds/detail', get_location_array),
    path('profile', get_watcher_profile),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))

]
