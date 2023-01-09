from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    description = models.TextField()

    salary = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)
    JOBTYPE_OPTION = [
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    ]
    jobtype = models.CharField(max_length=50,default='Full Time',choices=JOBTYPE_OPTION)

    locations = models.OneToOneField('jobapp.Location', on_delete=models.CASCADE)
    authors = models.ForeignKey('jobapp.Author', on_delete=models.CASCADE)
    skills = models.ManyToManyField('jobapp.Skill')

    class Meta:
        verbose_name = 'JobPost'
        verbose_name_plural = 'JobPosts'

    def __str__(self):
        return self.title
# ------------
class Location(models.Model):
    street = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    country = models.CharField(max_length = 150)
    zip = models.IntegerField()
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.state
# ------------
class Author(models.Model):
    name = models.CharField(max_length = 150)
    company = models.CharField(max_length = 150)
    designation = models.CharField(max_length = 150)
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name
# ------------
class Skill(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name