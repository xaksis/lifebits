from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from lifebits.models import User, List
from django.contrib import admin
from rest_framework import viewsets, routers
from lifebits import views

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'items', views.ItemViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
 url(r'^', include(router.urls)),
 #url(r'^$', ListView.as_view(
 #       queryset=User.objects.all(),
 #       context_object_name="users_list"),
 #       name="home"
 #   ),
 #url(r'^user/(?P<slug>[a-zA-Z0-9-]+)/$', DetailView.as_view(
 #       slug_field="handle",
 #       queryset=User.objects.all(),
 #       context_object_name="user"),
 #       name="user"
 #   ),
    # Examples:
    # url(r'^$', 'lifebits.views.home', name='home'),
    # url(r'^lifebits/', include('lifebits.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
