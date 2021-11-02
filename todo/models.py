from django.db import models

# Create your models here.


class Item(models.Model):
    # Item(models.Model) means it inherits from the Model class
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Overrides the model string method to show item's name instead
    def __str__(self):
        return self.name