"""drfElevator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from elevator import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"elevator", views.ElevatorViewSet, basename="elevator")
router.register(r"request", views.RequestViewSet, basename="request")

routes = router.get_routes(views.ElevatorViewSet)
# for route in routes:
#     print(route.url, route.mapping)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/elevator/bulk_create_elevators/",
        views.ElevatorViewSet.as_view({"post": "bulk_create_elevators"}),
    ),
    path(
        "api/elevator/<int:pk>/set_operational/<int:is_operational>/",
        views.ElevatorViewSet.as_view({"post": "set_operational"}),
        name="elevator_set_operational",
    ),
    path(
        "api/elevator/<int:pk>/set_door_status/<int:is_door_open>/",
        views.ElevatorViewSet.as_view({"post": "set_door_status"}),
        name="elevator_set_door_status",
    ),
    path(
        "elevator/<int:pk>/requests/",
        views.ElevatorViewSet.as_view({"get": "requests"}),
        name="elevator-requests",
    ),
]
