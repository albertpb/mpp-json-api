from rest_framework.routers import DefaultRouter
from mpp.api.views import UploadViewSet

router_mpp = DefaultRouter()

router_mpp.register(prefix='mpp', basename='mpp', viewset=UploadViewSet)