from django.db import migrations


# Apps whose model permissions (add/change/delete/view) we grant to operation_leads.
# Excludes: auth (except specific user perms), admin log, contenttypes, sessions.
ALLOWED_APPS = {
    'crm',
    'common',
    'tasks',
    'analytics',
    'massmail',
    'chat',
    'voip',
}

# Explicit extra permissions beyond the ALLOWED_APPS coverage.
EXTRA_PERMISSIONS = [
    ('auth', 'view_user'),
    ('auth', 'add_user'),
    ('auth', 'change_user'),
]

# Permissions the group must NEVER receive (enforced by explicit exclusion).
DENIED_PERMISSIONS = {
    ('auth', 'add_permission'),
    ('auth', 'change_permission'),
    ('auth', 'delete_permission'),
    ('auth', 'view_permission'),
    ('auth', 'delete_user'),
    ('auth', 'add_group'),
    ('auth', 'change_group'),
    ('auth', 'delete_group'),
    ('auth', 'view_group'),
}


def create_operation_leads_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    group, _ = Group.objects.get_or_create(name='operation_leads')

    # All permissions for the allowed apps
    allowed_cts = ContentType.objects.filter(app_label__in=ALLOWED_APPS)
    perms = list(Permission.objects.filter(content_type__in=allowed_cts))

    # Specific auth permissions for user management (add/change/view user)
    extra_codenames = [codename for _, codename in EXTRA_PERMISSIONS]
    extra_perms = Permission.objects.filter(
        content_type__app_label='auth',
        codename__in=extra_codenames,
    )
    perms.extend(extra_perms)

    # Remove any denied permissions
    final_perms = [
        p for p in perms
        if (p.content_type.app_label, p.codename) not in DENIED_PERMISSIONS
    ]

    group.permissions.set(final_perms)


def remove_operation_leads_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='operation_leads').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_product_company_and_campaign_product'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(
            create_operation_leads_group,
            remove_operation_leads_group,
        ),
    ]
