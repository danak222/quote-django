from django.db import models

# TODO 6: Create a Quote model with:
#   - text (CharField, max_length=500)
#   - author (CharField, max_length=100)
#   - __str__ method that returns the text

class Quote(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text