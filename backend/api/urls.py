from rest_framework.routers import DefaultRouter

from api.views import GoodViewSet, PriceViewSet, TypeViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'goods', GoodViewSet, basename='good')
router.register(r'prices', PriceViewSet, basename='price')
router.register(r'types', TypeViewSet, basename='type')

urlpatterns = router.urls
