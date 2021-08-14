from django.conf.urls import url
from .views import doibongApi,cauthuApi,SaveFile,overallApi,ageApi,areaApi,heightweightApi

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^doibong/([0-9]+)$', doibongApi),
    url(r'^doibong',doibongApi),

    url(r'^cauthu/savefile',SaveFile),
    url(r'^cauthu/([0-9]+)$',cauthuApi),
    url(r'^cauthu',cauthuApi),

    url(r'^overall', overallApi),
    url(r'^age', ageApi),
    url(r'^area', areaApi),
    url(r'^height_weight', heightweightApi),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)