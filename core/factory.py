import factory
from faker import Faker

from core.models import Patient

faker = Faker()


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    first_name = factory.LazyAttribute(lambda _: faker.name())
    gender = factory.LazyAttribute(lambda _: faker.random.choice(("Мужской", "Женский")))
    second_name = factory.LazyAttribute(lambda _: faker.name())
