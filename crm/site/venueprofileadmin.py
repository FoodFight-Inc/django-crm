from django.contrib import admin
from crm.site.crmmodeladmin import CrmModelAdmin
from crm.models.venue_profile import VenueProfile


class VenueProfileAdmin(CrmModelAdmin):
    list_display = ('company', 'venue_type', 'launch_status', 'capacity',
                    'supports_sampling', 'team_affiliations')
    list_filter = ('venue_type', 'launch_status', 'supports_sampling',
                   'has_qr_placement', 'staff_incentive_enabled')
    search_fields = ('company__full_name', 'team_affiliations')
    fieldsets = (
        (None, {
            'fields': ('company', 'venue_type', 'capacity')
        }),
        ('Traffic', {
            'fields': ('avg_game_day_traffic', 'avg_weekend_traffic')
        }),
        ('Capabilities', {
            'fields': (
                'supports_sampling', 'has_qr_placement', 'has_tv_audio',
                'has_patio', 'kitchen_open_late', 'staff_incentive_enabled',
            )
        }),
        ('Status', {
            'fields': ('launch_status', 'team_affiliations')
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


class VenueProfileInline(admin.StackedInline):
    model = VenueProfile
    extra = 0
    can_delete = False
    fields = (
        'venue_type', 'capacity',
        'avg_game_day_traffic', 'avg_weekend_traffic',
        'supports_sampling', 'has_qr_placement', 'has_tv_audio',
        'has_patio', 'kitchen_open_late', 'staff_incentive_enabled',
        'launch_status', 'team_affiliations',
    )
