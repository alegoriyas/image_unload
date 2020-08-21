"""
Definition of urls for core.
"""

from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static
from core.views import BookListView

urlpatterns = [
    #Page home (index)
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/upload/$', views.upload_book, name='upload_book'),
    url(r'^books/(?P<pk>\d+)/$', views.delete_book, name='delete_book'),
    
    url(r'^class/books/$', BookListView.as_view(), name='class_book_list'),
    url(r'^class/books/upload/$', views.UploadBookView.as_view(), name='class_upload_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)