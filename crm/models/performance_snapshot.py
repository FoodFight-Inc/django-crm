from django.db import models
from common.models import Base1


class PerformanceSnapshot(Base1):
    campaign = models.ForeignKey(
        'crm.ActivationCampaign', on_delete=models.CASCADE,
        related_name='snapshots')
    period_start = models.DateField()
    period_end = models.DateField()
    signups = models.PositiveIntegerField(default=0)
    entries = models.PositiveIntegerField(default=0)
    redemptions = models.PositiveIntegerField(default=0)
    staff_referrals = models.PositiveIntegerField(default=0)
    estimated_incremental_sales = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    estimated_impressions = models.PositiveIntegerField(null=True, blank=True)
    repeat_user_rate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True,
        help_text="Percentage"
    )
    venue_roi_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Performance Snapshot'
        verbose_name_plural = 'Performance Snapshots'
        ordering = ['-period_start']

    def __str__(self):
        return f"{self.campaign} ({self.period_start} – {self.period_end})"
