from django.contrib import admin
from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.activation_campaign import ActivationCampaign


class ActivationCampaignAdmin(CrmModelAdmin):
    list_display = ('name', 'deal', 'campaign_type', 'launch_status',
                    'creative_status', 'compliance_status', 'start_date', 'end_date')
    list_filter = ('campaign_type', 'launch_status', 'creative_status',
                   'compliance_status', 'reporting_status', 'offer_type')
    search_fields = ('name', 'deal__name', 'sports_moment')
    raw_id_fields = ('deal', 'sponsor_account')
    filter_horizontal = ('venue_accounts',)
    fieldsets = (
        (None, {
            'fields': ('name', 'deal', ('campaign_type', 'offer_type'),
                       'sports_moment', 'cta_type')
        }),
        ('Dates', {
            'fields': (('start_date', 'end_date'),)
        }),
        ('Accounts', {
            'fields': ('sponsor_account', 'venue_accounts')
        }),
        ('Status', {
            'fields': (
                ('creative_status', 'compliance_status'),
                ('launch_status', 'reporting_status'),
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
    readonly_fields = ('modified_by', 'creation_date', 'update_date')


class ActivationCampaignInline(admin.StackedInline):
    model = ActivationCampaign
    extra = 0
    show_change_link = True
    fields = (
        'name', 'campaign_type', 'offer_type',
        ('start_date', 'end_date'),
        ('creative_status', 'compliance_status', 'launch_status'),
    )
