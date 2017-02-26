from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
	url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
  	url(r'^about/', views.About.as_view(), name='about'),
	url(r'^agenda/', include('agenda.urls', namespace='agenda')),
	url(r'^maestras/', include('maestras.urls', namespace='maestras')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
