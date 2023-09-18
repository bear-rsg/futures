from django.views.generic import (ListView, DetailView)
from . import models


class InspirationListView(ListView):
    """
    Inspiration: List
    Class-based view to show the inspiration list template
    """

    template_name = 'inspirations/inspiration-list.html'
    queryset = models.Inspiration.objects.filter(admin_published=True)


class InspirationDetailView(DetailView):
    """
    Inspiration: Detail
    Class-based view to show the inspiration detail template
    """
    template_name = 'inspirations/inspiration-detail.html'
    queryset = models.Inspiration.objects.filter(admin_published=True)
