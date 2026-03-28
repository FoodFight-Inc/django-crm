from django.db import models
from common.models import Base1


class VenueProfile(Base1):
    company = models.OneToOneField(
        'crm.Company', on_delete=models.CASCADE, related_name='venue_profile')
    venue_type = models.CharField(
        max_length=30, null=True, blank=True,
        choices=[
            ('sports_bar', 'Sports Bar'),
            ('restaurant', 'Restaurant'),
            ('hotel_bar', 'Hotel Bar'),
            ('alumni_bar', 'Alumni Bar'),
            ('campus', 'Campus'),
            ('entertainment', 'Entertainment Venue'),
        ]
    )
    capacity = models.PositiveIntegerField(null=True, blank=True)
    avg_game_day_traffic = models.PositiveIntegerField(null=True, blank=True)
    avg_weekend_traffic = models.PositiveIntegerField(null=True, blank=True)
    team_affiliations = models.CharField(max_length=255, null=True, blank=True)
    supports_sampling = models.BooleanField(null=True, blank=True)
    has_qr_placement = models.BooleanField(null=True, blank=True)
    has_tv_audio = models.BooleanField(null=True, blank=True)
    has_patio = models.BooleanField(null=True, blank=True)
    kitchen_open_late = models.BooleanField(null=True, blank=True)
    staff_incentive_enabled = models.BooleanField(null=True, blank=True)
    launch_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=[
            ('not_launched', 'Not Launched'),
            ('in_setup', 'In Setup'),
            ('live', 'Live'),
            ('paused', 'Paused'),
        ]
    )

    class Meta:
        verbose_name = 'Venue Profile'
        verbose_name_plural = 'Venue Profiles'

    def __str__(self):
        return f"Venue Profile: {self.company}"
