from django.db import models


# Create model of university classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # Create model manager
    object = models.Manager()

    # Displays the object output values as a string form
    def __str__(self):
        # Returns input values  of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Remove the added 's' that Django adds to model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"

