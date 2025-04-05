from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Ley


class LeyListView(ListView):
    model = Ley
    template_name = "leyes/ley_list.html"
    context_object_name = "leyes"


class LeyDetailView(DetailView):
    model = Ley
    template_name = "leyes/ley_detail.html"
    context_object_name = "ley"
