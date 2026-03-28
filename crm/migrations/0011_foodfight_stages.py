from django.db import migrations

FOODFIGHT_STAGES = [
    ('Prospecting', 1, True, False),
    ('Discovery', 2, False, False),
    ('Qualified', 3, False, False),
    ('Compliance Review', 4, False, False),
    ('Proposal Sent', 5, False, False),
    ('Budget Alignment', 6, False, False),
    ('Pilot Structured', 7, False, False),
    ('Contracting', 8, False, False),
    ('Launch Prep', 9, False, False),
    ('Live Campaign', 10, False, False),
    ('Expansion', 11, False, False),
    ('Closed Won', 12, False, True),
    ('Closed Lost', 13, False, False),
    ('On Hold', 14, False, False),
]


def create_foodfight_stages(apps, schema_editor):
    Stage = apps.get_model('crm', 'Stage')
    Group = apps.get_model('auth', 'Group')

    departments = Group.objects.filter(department__isnull=False)
    if not departments.exists():
        # No departments yet — stages will need to be added via admin after setup
        return

    for department in departments:
        for name, index, is_default, is_success in FOODFIGHT_STAGES:
            if not Stage.objects.filter(name=name, department=department).exists():
                Stage.objects.create(
                    name=name,
                    index_number=index,
                    default=is_default,
                    success_stage=is_success,
                    department=department,
                )


def remove_foodfight_stages(apps, schema_editor):
    Stage = apps.get_model('crm', 'Stage')
    stage_names = [name for name, *_ in FOODFIGHT_STAGES]
    Stage.objects.filter(name__in=stage_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_foodfight_fields_and_models'),
    ]

    operations = [
        migrations.RunPython(create_foodfight_stages, remove_foodfight_stages),
    ]
