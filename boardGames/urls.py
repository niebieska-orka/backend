"""boardGames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from boardGames.rental import views
from django.contrib import admin

from boardGames.rental.views import ReservationApiView, ReservationApiView2, PersonApiView2, GameApiView2, PersonApiView, GameApiView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'games', views.GameViewSet)
#router.register(r'reservation', ReservationApiView.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('rental/', include('boardGames.rental.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reservation/<pk>', ReservationApiView.as_view()),
    path('reservation/', ReservationApiView2.as_view()),
    path('game/', GameApiView2.as_view()),
    path('person/', PersonApiView2.as_view()),
    path('game/<pk>', GameApiView.as_view()),
    path('person/<pk>', PersonApiView.as_view()),
]