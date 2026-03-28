from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.performance_snapshot import PerformanceSnapshot


class PerformanceSnapshotAdmin(CrmModelAdmin):
    list_display = ('campaign', 'period_start', 'period_end',
                    'signups', 'entries', 'redemptions', 'staff_referrals',
                    'estimated_incremental_sales', 'repeat_user_rate')
    list_filter = ('campaign__campaign_type',)
    search_fields = ('campaign__name', 'venue_roi_notes')
    raw_id_fields = ('campaign',)
    fieldsets = (
        (None, {
            'fields': ('campaign', ('period_start', 'period_end'))
        }),
        ('Metrics', {
            'fields': (
                ('signups', 'entries', 'redemptions', 'staff_referrals'),
                ('estimated_incremental_sales', 'estimated_impressions'),
                'repeat_user_rate',
            )
        }),
        ('Notes', {
            'fields': ('venue_roi_notes',)
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
