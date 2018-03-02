from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from FriendsFinder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^FriendsFinder/', include('FriendsFinder.urls')),
	# above maps any URLs starting
	# with FriendsFinder/ to be handled by
	# the FriendsFinder application
	url(r'^admin/', admin.site.urls),
	url(r'^social_auth/', include("social_django.urls", namespace="social")),
	


	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)