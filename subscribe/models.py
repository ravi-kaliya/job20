from django.db import models
# Create your models here.
class Subscribe(models.Model):
    fname = models.CharField(max_length = 150)
    lname = models.CharField(max_length = 150)
    email = models.EmailField()
    SUBSCRIPTION_OPTION = [
        ('Weekly','Weekly',),
        ('Monthly','Monthly',),
    ]
    option = models.CharField(max_length = 150, default='Monthly', choices = SUBSCRIPTION_OPTION )


    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'

    def __str__(self):
        return self.email