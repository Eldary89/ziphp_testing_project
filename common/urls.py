from rest_framework.routers import DefaultRouter
from .views import AirplaneModelViewSet


app_name = 'common'
router = DefaultRouter()
router.register(r"airplane", AirplaneModelViewSet, "airplane")

urlpatterns = router.urls
