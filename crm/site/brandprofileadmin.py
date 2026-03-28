from django.contrib import admin
from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.brand_profile import BrandProfile


class BrandProfileAdmin(CrmModelAdmin):
    list_display = ('company', 'brand_category', 'priority_markets',
                    'consumer_budget', 'trade_budget')
    list_filter = ('brand_category',)
    search_fields = ('company__full_name', 'portfolio_names', 'priority_markets')
    fieldsets = (
        (None, {
            'fields': ('company', 'brand_category', 'portfolio_names')
        }),
        ('Markets & Budget', {
            'fields': (
                'priority_markets',
                ('consumer_budget', 'trade_budget'),
            )
        }),
        ('Notes', {
            'fields': (
                'distributor_network_notes',
                'reporting_requirements',
                'legal_constraints_notes',
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


class BrandProfileInline(admin.StackedInline):
    model = BrandProfile
    extra = 0
    can_delete = False
    fields = (
        'brand_category', 'portfolio_names', 'priority_markets',
        ('consumer_budget', 'trade_budget'),
        'distributor_network_notes', 'reporting_requirements',
        'legal_constraints_notes',
    )
