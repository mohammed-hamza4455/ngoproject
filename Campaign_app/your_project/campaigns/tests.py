from django.test import TestCase
from .models import Campaign

class CampaignModelTest(TestCase):
    def test_str_representation(self):
        campaign = Campaign(title="Test Campaign")
        self.assertEqual(str(campaign), campaign.title)
