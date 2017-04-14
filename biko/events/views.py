# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from events.forms import EventForm
from events.models import Event


class EventCreateView(CreateView):
    template_name = 'events/new_event.html'
    form_class = EventForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        self.object.create_recurrent_events()
        return super(EventCreateView, self).form_valid(form)


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        return context


class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = {}
        context['events'] = Event.objects.filter(main_event__isnull=True)
        return context


class SearchEventListView(ListView):
    template_name = 'events/event_results.html'
    model = Event

    def get_context_data(self, **kwargs):
        date_str = self.request.GET.get('date', None)
        if date_str:
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
            context = {}
            context['events'] = Event.objects.filter(date=date_object)
            context['date'] = date_str
        return context
