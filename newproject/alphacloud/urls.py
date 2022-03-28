from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from alphacloud import views

urlpatterns = [
    # path('', views.alphacloud_list),
    # path('alphacloud/<int:pk>/', views.alphacloud_detail),

    path('alphacloud/', views.AlphacloudListCbv.as_view()),
    path('alphacloud/<int:pk>/', views.AlphacloudUpdateCbv.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)