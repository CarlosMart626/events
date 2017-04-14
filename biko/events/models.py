# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import calendar
from dateutil.relativedelta import relativedelta

from django.db import models
from django.conf import settings


class Event(models.Model):
    main_event = models.ForeignKey("self", null=True, blank=True)
    name = models.CharField(max_length=140)
    date = models.DateField()

    def __unicode__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    def create_recurrent_events(self):

        def is_valid_first_week(month_calendar):
            if month_calendar[0].count(0) > 3:
                return False
            return True

        current_date = self.date
        for n in range(settings.RECURRENT_EVENTS):
            current_date = current_date + relativedelta(months=1)
            month_calendar = calendar.monthcalendar(current_date.year, current_date.month)
            if is_valid_first_week(month_calendar):
                current_date = current_date.replace(day=month_calendar[1][self.date.weekday()])
            else:
                current_date = current_date.replace(day=month_calendar[2][self.date.weekday()])
            Event.objects.create(
                main_event=self,
                name="Repetition[{}] - {}".format(n + 1, self.name),
                date=current_date
            )

    @property
    def get_repetitions(self):
        return Event.objects.filter(main_event=self)
