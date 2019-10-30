from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from post import mixin_views

# router = DefaultRouter()
# router.register('post', views.PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
#     path('post/',mixin_views.PostList.as_view()),
#     path('post/<int:pk>/',mixin_views.PostDetail.as_view()),
# ]

# urlpatterns  = format_suffix_patterns(urlpatterns)
