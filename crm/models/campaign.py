from django.db import models
from common.models import Base1


class Campaign(Base1):

    STATUS_DRAFT = 'draft'
    STATUS_SCHEDULED = 'scheduled'
    STATUS_ACTIVE = 'active'
    STATUS_PAUSED = 'paused'
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    OFFER_CHOICES = [
        ('beer', 'Beer'),
        ('spirits', 'Spirits'),
        ('shot', 'Shot'),
        ('food', 'Food'),
        ('prize', 'Prize'),
        ('coupon', 'Coupon / Discount'),
        ('merch', 'Merch'),
        ('other', 'Other'),
    ]

    LEAGUE_CHOICES = [
        ('nfl', 'NFL'),
        ('cfb', 'College Football'),
        ('nba', 'NBA'),
        ('mlb', 'MLB'),
        ('nhl', 'NHL'),
        ('ufc', 'UFC'),
        ('soccer', 'Soccer'),
        ('march_madness', 'March Madness'),
        ('other', 'Other'),
    ]

    GAME_SCHEDULE_CHOICES = [
        ('any', 'Any Game'),
        ('specific_date', 'Specific Date'),
        ('monday_night', 'Monday Night Football'),
        ('super_bowl', 'Super Bowl'),
        ('march_madness', 'March Madness'),
        ('opening_day', 'Opening Day'),
        ('playoffs', 'Playoffs'),
        ('championship', 'Championship'),
        ('season', 'Full Season'),
        ('preseason', 'Preseason'),
        ('first_half', 'First Half of Season'),
        ('second_half', 'Second Half of Season'),
        ('happy_hour', 'Happy Hour'),
        ('other', 'Other'),
    ]

    # Identity
    name = models.CharField(max_length=255)
    company = models.ForeignKey(
        'crm.Company', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='campaigns',
        help_text="Brand or venue company this campaign belongs to"
    )
    contact = models.ForeignKey(
        'crm.Contact', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='campaigns',
        help_text="Brand contact"
    )
    parent_campaign = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='sub_campaigns',
        help_text="Parent campaign (e.g. full season) this is a sub-campaign of"
    )
    deal = models.ForeignKey(
        'crm.Deal', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='promo_campaigns'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT
    )
    notes = models.TextField(null=True, blank=True)

    # Offer
    offer_type = models.CharField(
        max_length=20, null=True, blank=True, choices=OFFER_CHOICES
    )
    offer_description = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="e.g. 'Free beer', '$2 off happy hour'"
    )
    offer_value = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True,
        help_text="Monetary value per offer (for coupons/discounts)"
    )

    # Schedule
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Sport criteria
    league = models.CharField(
        max_length=20, null=True, blank=True, choices=LEAGUE_CHOICES
    )
    team = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="e.g. Bears, Michigan"
    )
    game_schedule_type = models.CharField(
        max_length=30, null=True, blank=True, choices=GAME_SCHEDULE_CHOICES
    )

    # Promo limits (null = unlimited)
    max_global = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Total promos available across all venues. Leave blank for unlimited."
    )
    max_per_venue = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Max promos per venue. Leave blank for unlimited."
    )
    max_per_individual = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Max promos per individual. Leave blank for unlimited."
    )

    # Tracking
    redeemed_count = models.PositiveIntegerField(default=0)
    active_count = models.PositiveIntegerField(
        default=0, help_text="Currently active / in-flight promos"
    )
    invoiced_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        help_text="Manual invoiced total (budget or units)"
    )

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'
        ordering = ['-creation_date']

    def __str__(self):
        return self.name

    @property
    def estimated_count(self):
        return self.redeemed_count + self.active_count

    @property
    def is_depleted(self):
        if self.max_global is None:
            return False
        return self.estimated_count >= self.max_global


class CampaignVenue(Base1):
    """Maps a venue (Company) to a Campaign with venue-specific settings."""

    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name='campaign_venues'
    )
    venue = models.ForeignKey(
        'crm.Company', on_delete=models.CASCADE, related_name='campaign_venues'
    )
    venue_items = models.TextField(
        null=True, blank=True,
        help_text="Items available at this venue for the campaign"
    )
    max_override = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Venue-specific promo max (overrides campaign default)"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Campaign Venue'
        verbose_name_plural = 'Campaign Venues'
        unique_together = ('campaign', 'venue')

    def __str__(self):
        return f"{self.venue} — {self.campaign}"


class OutcomePool(Base1):
    """Defines what game outcomes trigger promo eligibility for a campaign."""

    SCOPE_CHOICES = [
        ('microtransaction', 'Microtransaction (e.g. Next Score)'),
        ('game_progression', 'Game Progression (e.g. Q1, Half)'),
        ('final_outcome', 'Final Outcome (Win / Loss)'),
    ]

    TYPE_CHOICES = [
        ('next_score', 'Next Score'),
        ('next_td', 'Next Touchdown'),
        ('next_fg', 'Next Field Goal'),
        ('q1', 'End of Q1'),
        ('q2', 'End of Q2'),
        ('halftime', 'Halftime'),
        ('q3', 'End of Q3'),
        ('q4', 'End of Q4 / Final'),
        ('win', 'Win'),
        ('loss', 'Loss'),
        ('any', 'Any Outcome'),
        ('other', 'Other'),
    ]

    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name='outcome_pools'
    )
    scope = models.CharField(max_length=30, choices=SCOPE_CHOICES)
    outcome_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Outcome Pool'
        verbose_name_plural = 'Outcome Pools'

    def __str__(self):
        return f"{self.campaign} — {self.get_outcome_type_display()}"


class PromoTarget(Base1):
    """Queue of promos not yet live but scheduled to go live at set increments."""

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('live', 'Live'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name='promo_targets'
    )
    scheduled_for = models.DateTimeField()
    promo_count = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Promo Target'
        verbose_name_plural = 'Promo Targets'
        ordering = ['scheduled_for']

    def __str__(self):
        return f"{self.campaign} — {self.scheduled_for:%Y-%m-%d %H:%M} ({self.promo_count})"
