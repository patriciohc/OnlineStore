from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from api_rest.views import ProductViewSet, CategoryList, ImageViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'image', ImageViewSet)


urlpatterns = [
	#url(r'^product/(?P<category>.+)/$', views.ProductList.as_view()),
    #url(r'^product/$', ProductList.as_view()),
    url(r'^', include(router.urls)),
    url(r'^categories/$', CategoryList.as_view()),
    url(r'^token-auth/$', 'rest_framework.authtoken.views.obtain_auth_token'),
    #url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
