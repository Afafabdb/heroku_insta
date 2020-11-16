from django.urls import path, re_path
from insta_app import views

app_name = 'insta_app'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^code/$', views.code, name='code'),
    # insta registering
    # re_path(r'^insta/reg/$',
    #         views.insta_reg, name='insta_reg'),

    re_path(r'^instagram/(?P<name>([A-Za-z0-9\-\_]+))/$',
            views.instagram_some, name='instagram_some'),
]
'''
    url(r'^create/$', views.main_create_log_in, name='create'),
'''
