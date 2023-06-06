from django.test import TestCase

from core.factory import PatientFactory
from core.models import Patient


class PatientTestCase(TestCase):
    def setUp(self):
        self.test_patient = PatientFactory.create()

    def test_Patient(self):
        self.assertEqual(self.test_patient.first_name, Patient.objects.get(id=1).first_name)
