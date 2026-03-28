from django.contrib import admin
from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.campaign import Campaign, CampaignVenue, OutcomePool, PromoTarget


class CampaignVenueInline(admin.TabularInline):
    model = CampaignVenue
    extra = 0
    fields = ('venue', 'venue_items', 'max_override', 'is_active')
    raw_id_fields = ('venue',)


class OutcomePoolInline(admin.TabularInline):
    model = OutcomePool
    extra = 0
    fields = ('scope', 'outcome_type', 'description')


class PromoTargetInline(admin.TabularInline):
    model = PromoTarget
    extra = 0
    fields = ('scheduled_for', 'promo_count', 'status', 'notes')


class CampaignAdmin(CrmModelAdmin):
    list_display = (
        'name', 'status', 'company', 'contact',
        'offer_type', 'league', 'team', 'game_schedule_type',
        'start_date', 'end_date',
        'max_global', 'redeemed_count', 'active_count',
    )
    list_filter = (
        'status', 'offer_type', 'league', 'game_schedule_type',
    )
    search_fields = (
        'name', 'company__full_name', 'contact__first_name',
        'contact__last_name', 'team', 'notes',
    )
    raw_id_fields = ('company', 'contact', 'deal', 'parent_campaign')
    inlines = [CampaignVenueInline, OutcomePoolInline, PromoTargetInline]
    readonly_fields = ('modified_by', 'creation_date', 'update_date')
    fieldsets = (
        (None, {
            'fields': (
                'name', 'status',
                ('company', 'contact'),
                ('deal', 'parent_campaign'),
                'notes',
            )
        }),
        ('Offer', {
            'fields': (
                ('offer_type', 'offer_description', 'offer_value'),
            )
        }),
        ('Schedule', {
            'fields': (
                ('start_date', 'end_date'),
            )
        }),
        ('Sport Criteria', {
            'fields': (
                ('league', 'team'),
                'game_schedule_type',
            )
        }),
        ('Promo Limits', {
            'fields': (
                ('max_global', 'max_per_venue', 'max_per_individual'),
            )
        }),
        ('Tracking', {
            'fields': (
                ('redeemed_count', 'active_count', 'invoiced_amount'),
            )
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': (
                ('owner', 'department'),
                'modified_by',
                ('creation_date', 'update_date'),
            )
        }),
    )


class CampaignVenueAdmin(CrmModelAdmin):
    list_display = ('campaign', 'venue', 'max_override', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('campaign__name', 'venue__full_name')
    raw_id_fields = ('campaign', 'venue')
    readonly_fields = ('modified_by', 'creation_date', 'update_date')


class OutcomePoolAdmin(CrmModelAdmin):
    list_display = ('campaign', 'scope', 'outcome_type')
    list_filter = ('scope', 'outcome_type')
    search_fields = ('campaign__name', 'description')
    raw_id_fields = ('campaign',)
    readonly_fields = ('modified_by', 'creation_date', 'update_date')


class PromoTargetAdmin(CrmModelAdmin):
    list_display = ('campaign', 'scheduled_for', 'promo_count', 'status')
    list_filter = ('status',)
    search_fields = ('campaign__name', 'notes')
    raw_id_fields = ('campaign',)
    readonly_fields = ('modified_by', 'creation_date', 'update_date')
