from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client', views.ClientView)
router.register('user', views.UserView)
router.register('location', views.LocationView)
router.register('test_standard', views.TestStandardView)
router.register('product', views.ProductView)
router.register('test_sequence', views.TestSequenceView)
router.register('performance_data', views.PerformanceDataView)
router.register('service', views.ServiceView)
router.register('certificate', views.CertificateView)
#router.register('test', views.TestView.as_view(), basename='Test')

urlpatterns = [
    url(r'^api/', include(router.urls))
]
