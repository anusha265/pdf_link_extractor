from django.urls import path
from link_extractor.views import extract_links

app_name = 'link_extractor'

urlpatterns = [
    path('', extract_links, name='extract_links'),
]
