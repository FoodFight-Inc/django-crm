from django.db import models
from common.models import Base1


class CampaignProduct(Base1):
    """
    Links a Product to a Campaign with per-campaign allocation,
    redemption, and invoice tracking.
    """

    INVOICE_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('disputed', 'Disputed'),
        ('void', 'Void'),
    ]

    BILLED_TO_CHOICES = [
        ('brand', 'Brand'),
        ('venue', 'Venue'),
        ('foodfight', 'FoodFight'),
        ('split', 'Split'),
    ]

    campaign = models.ForeignKey(
        'crm.Campaign', on_delete=models.CASCADE,
        related_name='campaign_products'
    )
    product = models.ForeignKey(
        'crm.Product', on_delete=models.CASCADE,
        related_name='campaign_products'
    )

    # Allocation & fulfillment
    units_allocated = models.PositiveIntegerField(
        default=0,
        help_text="Units committed to this campaign"
    )
    units_redeemed = models.PositiveIntegerField(
        default=0,
        help_text="Units actually redeemed"
    )
    units_invoiced = models.PositiveIntegerField(
        default=0,
        help_text="Units included on invoice (may differ from redeemed)"
    )

    # Pricing overrides
    unit_cost_override = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Campaign-specific unit cost (overrides product default)"
    )
    unit_retail_override = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Campaign-specific retail value (overrides product default)"
    )

    # Billing
    billed_to = models.CharField(
        max_length=20, null=True, blank=True, choices=BILLED_TO_CHOICES
    )
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    invoice_status = models.CharField(
        max_length=20, null=True, blank=True,
        choices=INVOICE_STATUS_CHOICES, default='pending'
    )
    invoice_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Campaign Product'
        verbose_name_plural = 'Campaign Products'
        unique_together = ('campaign', 'product')

    def __str__(self):
        return f"{self.product} — {self.campaign}"

    @property
    def effective_unit_cost(self):
        return self.unit_cost_override or (self.product.unit_cost or 0)

    @property
    def effective_unit_retail(self):
        return self.unit_retail_override or (self.product.unit_retail_value or 0)

    @property
    def total_cost(self):
        return self.effective_unit_cost * self.units_invoiced

    @property
    def total_retail_value(self):
        return self.effective_unit_retail * self.units_redeemed
