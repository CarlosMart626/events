# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.test import TestCase

from events.models import Event


class TestRecurrentEvents(TestCase):

    def test_create_event(self):
        event = Event.objects.create(
            name="Test Event",
            date=date(2017, 4, 7)
        )
        event.create_recurrent_events()
        self.assertEqual(event.get_repetitions.count(), 8)
        print("BEGIN\n")
        print(event.date)
        for event in event.get_repetitions:
            print(event.date)

    def test_number_events_created(self):
        event = Event.objects.create(
            name="Test Event",
            date=date(2017, 11, 07)
        )
        event.create_recurrent_events()
        self.assertEqual(event.get_repetitions.count(), 8)
        print("BEGIN\n")
        print(event.date)
        for event in event.get_repetitions:
            print(event.date)
