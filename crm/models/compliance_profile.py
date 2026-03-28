from django.db import models
from common.models import Base1


class ComplianceProfile(Base1):
    deal = models.ForeignKey(
        'crm.Deal', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='compliance_profiles')
    campaign = models.ForeignKey(
        'crm.ActivationCampaign', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='compliance_profiles')
    state_code = models.CharField(max_length=2)
    promotion_type = models.CharField(max_length=100, null=True, blank=True)
    full_size_allowed = models.BooleanField(null=True, blank=True)
    sample_only = models.BooleanField(null=True, blank=True)
    brand_funded_only = models.BooleanField(null=True, blank=True)
    venue_funded_allowed = models.BooleanField(null=True, blank=True)
    max_value_limit = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    counsel_review_required = models.BooleanField(default=False)
    counsel_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('not_started', 'Not Started'),
            ('in_review', 'In Review'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ]
    )
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Compliance Profile'
        verbose_name_plural = 'Compliance Profiles'

    def __str__(self):
        return f"Compliance: {self.state_code} — {self.promotion_type}"
