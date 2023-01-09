from faker import Faker
from jobapp.models import JobPost,Location,Author,Skill

fake = Faker()

for _ in range(0,5):
    Location.objects.create(street = fake.street_address(), state = fake.state(), city = fake.city(), country = fake.country(), zip = fake.postcode(), )
    Author.objects.create(name = fake.name(), company = fake.company(), designation = fake.job(), )