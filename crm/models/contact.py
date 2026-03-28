from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from common.models import Base1
from crm.models.base_contact import BaseContact
from crm.models.base_contact import BaseCounterparty


class Contact(BaseCounterparty, BaseContact, Base1):
    class Meta:
        verbose_name = _("Contact person")
        verbose_name_plural = _("Contact persons")

    company = models.ForeignKey(
        'Company', blank=False,
        null=False, on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name=_("Company of contact")
    )

    # FoodFight contact classification
    contact_role = models.CharField(
        max_length=30, null=True, blank=True,
        choices=[
            ('owner', 'Owner'),
            ('gm', 'General Manager'),
            ('beverage_manager', 'Beverage Manager'),
            ('marketing_manager', 'Marketing Manager'),
            ('brand_manager', 'Brand Manager'),
            ('field_marketer', 'Field Marketer'),
            ('distributor_rep', 'Distributor Rep'),
            ('agency_lead', 'Agency Lead'),
        ]
    )
    stakeholder_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('champion', 'Champion'),
            ('influencer', 'Influencer'),
            ('approver', 'Approver'),
            ('signer', 'Signer'),
            ('blocker', 'Blocker'),
        ]
    )
    decision_power_score = models.PositiveSmallIntegerField(
        null=True, blank=True, help_text="1–10")
    preferred_channel = models.CharField(
        max_length=10, null=True, blank=True,
        choices=[('text', 'Text'), ('email', 'Email'), ('phone', 'Phone')]
    )
    relationship_strength = models.CharField(
        max_length=10, null=True, blank=True,
        choices=[('weak', 'Weak'), ('neutral', 'Neutral'), ('strong', 'Strong')]
    )
    favorite_teams = models.CharField(max_length=255, null=True, blank=True)
    last_meeting_date = models.DateField(null=True, blank=True)

    @property
    def company_country(self):
        return self.company.country

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.company}, {self.country}"
    
    def get_absolute_url(self):  
        return reverse('admin:crm_contact_change', args=(self.id,))
