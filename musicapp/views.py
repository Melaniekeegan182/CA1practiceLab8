from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic  import DetailView
from.models import Band, Member, Song

# Createviews
class BandCreateView(CreateView):
    model = Band
    template_view = 'band_create.html'
    fields = ['name','nationality']

class MemberCreateView(CreateView):
    model = Member
    template_view = 'member_create.html'
    fields = ['name','dob', 'band']

class SongCreateView(CreateView):
    model = Song
    template_view = 'song_create.html'
    fields = ['title','author']  

# DetailView 
class BandDetailView(DetailView):
    model = Band
    template_name = 'band_detail.html'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'member_detail.html' 

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html' 


