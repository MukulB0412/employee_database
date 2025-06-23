from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data (optional)
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        departments = []
        for _ in range(5):
            dept = Department.objects.create(name=fake.job())
            departments.append(dept)

        # Create Employees + Attendance + Performance
        for _ in range(50):
            dept = random.choice(departments)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_this_decade(),
                department=dept
            )

            # Random attendance records
            for _ in range(5):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            # Random performance records
            for _ in range(2):
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_this_year()
                )

        self.stdout.write(self.style.SUCCESS("✅ Seeded 50 employees with related data"))

