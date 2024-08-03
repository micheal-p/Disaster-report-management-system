from django.db import models

class Report(models.Model):
    DISASTER_TYPE_CHOICES = [
        ('earthquake', 'Earthquake'),
        ('flood', 'Flood'),
        ('hurricane', 'Hurricane'),
        ('wildfire', 'Wildfire'),
        ('tornado', 'Tornado'),
        # Add other disaster types as needed
    ]

    disaster_type = models.CharField(max_length=50, choices=DISASTER_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='reports/images/', blank=True, null=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    is_legitimate = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.disaster_type} at {self.location}"
