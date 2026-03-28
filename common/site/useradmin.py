from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _


class CrmUserAdmin(UserAdmin):
    """
    User admin for the CRM site.
    Lets superusers and operation_leads create and manage users.
    The post_save signal automatically assigns the 'co-workers' group
    and creates a UserProfile for every new user.
    """

    # Fields shown on the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            ),
        }),
        (_('Role'), {
            'classes': ('wide',),
            'fields': ('groups', 'is_active', 'is_staff'),
        }),
    )

    # Fields shown on the change form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Role & access'), {'fields': ('is_active', 'is_staff', 'groups')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups',)

    # -- ModelAdmin methods -- #

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'groups':
            # Only show department-linked groups (roles), not internal system groups
            kwargs['queryset'] = Group.objects.order_by('name')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_operation_lead

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_operation_lead

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_operation_lead
