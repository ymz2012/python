from django.conf.urls import patterns, include, url

import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$',views.index),
    (r'^detail/(\d+)/$',views.bbs_detail),
)
