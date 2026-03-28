from django.db import migrations

FOODFIGHT_STAGES = [
    ('Prospecting', 1),
    ('Discovery', 2),
    ('Qualified', 3),
    ('Compliance Review', 4),
    ('Proposal Sent', 5),
    ('Budget Alignment', 6),
    ('Pilot Structured', 7),
    ('Contracting', 8),
    ('Launch Prep', 9),
    ('Live Campaign', 10),
    ('Expansion', 11),
    ('Closed Won', 12),
    ('Closed Lost', 13),
    ('On Hold', 14),
]


def create_foodfight_stages(apps, schema_editor):
    Stage = apps.get_model('crm', 'Stage')
    for name, index in FOODFIGHT_STAGES:
        if not Stage.objects.filter(name=name).exists():
            Stage.objects.create(
                name=name,
                index_number=index,
                default=(name == 'Prospecting'),
                success_stage=(name == 'Closed Won'),
            )


def remove_foodfight_stages(apps, schema_editor):
    Stage = apps.get_model('crm', 'Stage')
    stage_names = [name for name, _ in FOODFIGHT_STAGES]
    Stage.objects.filter(name__in=stage_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_foodfight_fields_and_models'),
    ]

    operations = [
        migrations.RunPython(create_foodfight_stages, remove_foodfight_stages),
    ]
