from django.urls import path
from link_extractor.views import extract_links

urlpatterns = [
    path('', extract_links, name='extract_links'),
]
