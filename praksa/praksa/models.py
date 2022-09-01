from django.db import models
from cms.models.fields import PlaceholderField

def my_placeholder_slotname(instance):
    return 'placeholder_name'

class MyModel(models.Model):
    # your fields
    my_placeholder = PlaceholderField(my_placeholder_slotname)
    # your methods