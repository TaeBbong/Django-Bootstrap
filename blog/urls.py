from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),

    url(r'^intro/', views.intro_page, name='intro_page'),

    url(r'^announce/$', views.announce_page, name='announce_page'),
    url(r'^announce/detail/(?P<pk>\d+)/$', views.announce_detail, name='announce_detail'),
    url(r'^announce/new/$', views.announce_new, name='announce_new'),

    url(r'^activity/', views.activity_page, name='activity_page'),

    url(r'^portfolio/', views.portfolio_page, name='portfolio_page'),

    url(r'^study/', views.study_page, name='study_page'),

    url(r'^seminar/', views.seminar_page, name='seminar_page'),

    url(r'^contact/', views.contact_page, name='contact_page'),
]

urlpatterns += static('media', document_root=settings.MEDIA_ROOT)