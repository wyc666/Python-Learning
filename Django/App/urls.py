from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bbs_detail/(\d+)/$', views.bbs_detail, name='bbs_detail'),

    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),
]