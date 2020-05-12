from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from dipno_backend.dipno.viewsets import UserViewSet, ProfileViewSet, MatchViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("profiles", ProfileViewSet)
router.register("matches", MatchViewSet)


app_name = "api"
urlpatterns = router.urls
