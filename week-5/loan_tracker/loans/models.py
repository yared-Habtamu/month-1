from django.db import models


# Create your models here.
class Loan(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_issued = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.name}  -  {self.amount}"
