from django.urls import path
from .views import BandCreateView, MemberCreateView, SongCreateView
from .views import BandDetailView, MemberDetailView, SongDetailView

urlpatterns = [
    path('newm/', MemberCreateView.as_view(), name='member_new'),
    path('newb/', BandCreateView.as_view(), name='band_new'),
    path('news/',SongCreateView.as_view(), name='song_new'),
    path('<int:pk>/', BandDetailView.as_view(), name='band_new'),
    path('m/<int:pk>/', MemberDetailView.as_view(), name='member_new'),
    path('s/<int:pk>/', SongDetailView.as_view(), name='song_new'),
]