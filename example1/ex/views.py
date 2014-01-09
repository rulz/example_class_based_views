from django.shortcuts import render
from django.views.generic.detail import DetailView
from datetime import datetime
from ex.models import Post


class HomeDetailView(DetailView):

    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

detail = HomeDetailView.as_view()
