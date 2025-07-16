from django.test import TestCase
from .models import Project
from django.utils import timezone

class ProjectModelTest(TestCase):
    def test_create_project(self):
        project = Project.objects.create(
            name="Test Project",
            description="Testing description",
            start_date=timezone.now(),
            end_date=timezone.now(),
            status="Planned"
        )
        self.assertEqual(project.name, "Test Project")
