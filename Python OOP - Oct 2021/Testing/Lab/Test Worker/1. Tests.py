from unittest import TestCase


class WorkerTests(TestCase):
    valid_name = "Worker 1"
    valid_salary = 1000
    valid_energy = 5

    def test_init__when_valid_name_salary_energy__expect_correctly_initialized(self):
        worker = Worker()