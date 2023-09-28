from django.urls import path, include
from .views import PostList, PostDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
     
app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/',include('users.urls'))
]
