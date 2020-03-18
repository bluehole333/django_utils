from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # 导入urls
    path('admin/', admin.site.urls),
    path('api/xxx/', include('xxxx.urls')),

    # 带参数
    path("api/<int:pk>/", views.xxxxxxxxAPIView.as_view()),
    path("api/<str:meta_type>/", views.xxxxxxxxAPIView.as_view()),

    # docs
    path('docs/', include_docs_urls(title='webtitle', public=True, description='',
                                    authentication_classes=[], permission_classes=[])),

    # url
    url(r'^(?P<pk>[0-9]+)/(?P<pk>[0-9]+)/list/', views.xxxxxxxxAPIView.as_view()),
    url(r'^xxxx/$', views.xxxxxxxxAPIView.as_view(), name='xxxx-list'),
    url(r'^$', views.xxxxxxxxAPIView.as_view(), name='index'),
]

# 修改默认的Django标题
admin.site.site_header = 'xxx系统后台'
admin.site.site_title = 'xxxx系统后台'
admin.site.index_title = '首页'
