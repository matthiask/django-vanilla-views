from django.conf.urls import patterns, url
from example.notes.views import ListNotes, CreateNote, EditNote, DeleteNote


urlpatterns = patterns(
    '',
    url(r'^$', ListNotes.as_view(), name='list_notes'),
    url(r'^create/$', CreateNote.as_view(), name='create_note'),
    url(r'^edit/(?P<pk>\d+)/$', EditNote.as_view(), name='edit_note'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteNote.as_view(), name='delete_note'),
)
