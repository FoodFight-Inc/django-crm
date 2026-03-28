from django.db import models
from common.models import Base1


class BrandProfile(Base1):
    company = models.OneToOneField(
        'crm.Company', on_delete=models.CASCADE, related_name='brand_profile')
    brand_category = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('beer', 'Beer'),
            ('spirits', 'Spirits'),
            ('rtd', 'RTD'),
            ('seltzer', 'Seltzer'),
            ('na', 'Non-Alcoholic'),
        ]
    )
    portfolio_names = models.CharField(max_length=255, null=True, blank=True)
    priority_markets = models.CharField(max_length=255, null=True, blank=True)
    distributor_network_notes = models.TextField(null=True, blank=True)
    consumer_budget = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    trade_budget = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    reporting_requirements = models.TextField(null=True, blank=True)
    legal_constraints_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Brand Profile'
        verbose_name_plural = 'Brand Profiles'

    def __str__(self):
        return f"Brand Profile: {self.company}"
