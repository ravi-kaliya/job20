from django.db import models

# Create your models here.
class Uploads(models.Model):
    image = models.ImageField(upload_to='upload_images',)
    description = models.CharField(max_length = 150)


    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'
    def __str__(self):
        return self.description

    # --------------------

class UploadsFiles(models.Model):
    file = models.FileField(upload_to = 'files',)
    description = models.CharField(max_length = 150)
    class Meta:
        verbose_name = 'UploadsFiles'
        verbose_name_plural = 'UploadsFiless'

    def __str__(self):
        return self.description