from django.db import models

# Create your models here.

from django.db import models

import ponytest

class CommaSepField(models.Field):
    "Implements comma-separated storage of lists"

    def __init__(self, separator=",", *args, **kwargs):
        self.separator = separator
        self.ponytest = ponytest
        super(CommaSepField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CommaSepField, self).deconstruct()
        # Only include kwarg if it's not the default
        if self.separator != ",":
            kwargs['separator'] = self.separator
        return name, path, args, kwargs


class M5(models.Model):
    f = models.IntegerField()

class M1(models.Model):
    f = models.IntegerField()

    csf = CommaSepField()


    def myfunc(self):
        return 1