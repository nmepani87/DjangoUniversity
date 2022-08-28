from django.db import models

# Create model of university campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Create model manager
    object = models.Manager()

    # Displays the object output values as a string form
    def __str__(self):
        # Returns input values  of the campus name and state
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name} - {0.state}'
        return display_campus.format(self)

    # Remove the added 's' that Django adds to model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
