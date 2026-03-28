from django.contrib import admin
from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.compliance_profile import ComplianceProfile


class ComplianceProfileAdmin(CrmModelAdmin):
    list_display = ('state_code', 'promotion_type', 'deal', 'campaign',
                    'counsel_status', 'counsel_review_required',
                    'full_size_allowed', 'sample_only')
    list_filter = ('state_code', 'counsel_status', 'counsel_review_required',
                   'full_size_allowed', 'sample_only', 'brand_funded_only')
    search_fields = ('state_code', 'promotion_type', 'notes',
                     'deal__name', 'campaign__name')
    raw_id_fields = ('deal', 'campaign')
    fieldsets = (
        (None, {
            'fields': (('deal', 'campaign'), ('state_code', 'promotion_type'))
        }),
        ('Rules', {
            'fields': (
                ('full_size_allowed', 'sample_only'),
                ('brand_funded_only', 'venue_funded_allowed'),
                'max_value_limit',
            )
        }),
        ('Counsel', {
            'fields': (
                ('counsel_review_required', 'counsel_status'),
                'notes',
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


class ComplianceProfileInline(admin.StackedInline):
    model = ComplianceProfile
    extra = 0
    show_change_link = True
    fields = (
        ('state_code', 'promotion_type'),
        ('full_size_allowed', 'sample_only', 'brand_funded_only'),
        ('counsel_review_required', 'counsel_status'),
        'notes',
    )
