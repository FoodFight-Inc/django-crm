from django.db import models
from common.models import Base1


class ActivationCampaign(Base1):
    deal = models.ForeignKey(
        'crm.Deal', on_delete=models.CASCADE, related_name='campaigns')
    name = models.CharField(max_length=255)
    campaign_type = models.CharField(
        max_length=30, null=True, blank=True,
        choices=[
            ('nfl', 'NFL'),
            ('cfb', 'College Football'),
            ('march_madness', 'March Madness'),
            ('ufc', 'UFC'),
            ('mlb', 'MLB'),
            ('opening_day', 'Opening Day'),
            ('world_cup', 'World Cup'),
            ('always_on', 'Always On'),
        ]
    )
    sports_moment = models.CharField(max_length=255, null=True, blank=True)
    offer_type = models.CharField(
        max_length=30, null=True, blank=True,
        choices=[
            ('free_sample', 'Free Sample'),
            ('discount', 'Discount'),
            ('merch', 'Merch'),
            ('bracket_promo', 'Bracket Promo'),
            ('trivia', 'Trivia'),
            ('prediction', 'Prediction'),
        ]
    )
    cta_type = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    sponsor_account = models.ForeignKey(
        'crm.Company', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='sponsored_campaigns')
    venue_accounts = models.ManyToManyField(
        'crm.Company', blank=True, related_name='venue_campaigns')
    creative_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('not_started', 'Not Started'),
            ('in_progress', 'In Progress'),
            ('approved', 'Approved'),
            ('live', 'Live'),
        ]
    )
    compliance_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('not_started', 'Not Started'),
            ('in_review', 'In Review'),
            ('approved', 'Approved'),
            ('blocked', 'Blocked'),
        ]
    )
    launch_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('not_launched', 'Not Launched'),
            ('in_setup', 'In Setup'),
            ('live', 'Live'),
            ('complete', 'Complete'),
        ]
    )
    reporting_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('complete', 'Complete'),
        ]
    )

    class Meta:
        verbose_name = 'Activation Campaign'
        verbose_name_plural = 'Activation Campaigns'

    def __str__(self):
        return self.name
