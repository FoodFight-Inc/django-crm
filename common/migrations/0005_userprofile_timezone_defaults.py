from django.db import migrations, models


def set_central_timezone(apps, schema_editor):
    UserProfile = apps.get_model('common', 'UserProfile')
    UserProfile.objects.filter(utc_timezone='').update(
        utc_timezone='America/Chicago',
        activate_timezone=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_reminder_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='utc_timezone',
            field=models.CharField(
                blank=True,
                choices=[
                    ('America/New_York', 'US Eastern (ET)'),
                    ('America/Chicago', 'US Central (CT)'),
                    ('America/Denver', 'US Mountain (MT)'),
                    ('America/Phoenix', 'US Mountain \u2013 no DST (AZ)'),
                    ('America/Los_Angeles', 'US Pacific (PT)'),
                    ('America/Anchorage', 'US Alaska (AKT)'),
                    ('Pacific/Honolulu', 'US Hawaii (HT)'),
                    ('Etc/GMT+12', 'UTC-12:00'),
                    ('Etc/GMT+11', 'UTC-11:00'),
                    ('Etc/GMT+10', 'UTC-10:00'),
                    ('Pacific/Marquesas', 'UTC-09:30'),
                    ('Etc/GMT+9', 'UTC-09:00'),
                    ('Etc/GMT+8', 'UTC-08:00'),
                    ('Etc/GMT+7', 'UTC-07:00'),
                    ('Etc/GMT+6', 'UTC-06:00'),
                    ('Etc/GMT+5', 'UTC-05:00'),
                    ('Etc/GMT+4', 'UTC-04:00'),
                    ('America/St_Johns', 'UTC-03:30'),
                    ('Etc/GMT+3', 'UTC-03:00'),
                    ('Etc/GMT+2', 'UTC-02:00'),
                    ('Etc/GMT+1', 'UTC-01:00'),
                    ('Etc/GMT0', 'UTC 00:00'),
                    ('Etc/GMT-1', 'UTC+01:00'),
                    ('Europe/Kiev', 'UTC+02:00'),
                    ('Etc/GMT-3', 'UTC+03:00'),
                    ('Asia/Tehran', 'UTC+03:30'),
                    ('Etc/GMT-4', 'UTC+04:00'),
                    ('Asia/Kabul', 'UTC+04:30'),
                    ('Etc/GMT-5', 'UTC+05:00'),
                    ('Asia/Kolkata', 'UTC+05:30'),
                    ('Asia/Kathmandu', 'UTC+05:45'),
                    ('Etc/GMT-6', 'UTC+06:00'),
                    ('Asia/Yangon', 'UTC+06:30'),
                    ('Etc/GMT-7', 'UTC+07:00'),
                    ('Etc/GMT-8', 'UTC+08:00'),
                    ('Australia/Eucla', 'UTC+08:45'),
                    ('Etc/GMT-9', 'UTC+09:00'),
                    ('Australia/Darwin', 'UTC+09:30'),
                    ('Etc/GMT-10', 'UTC+10:00'),
                    ('Australia/Lord_Howe', 'UTC+10:30'),
                    ('Etc/GMT-11', 'UTC+11:00'),
                    ('Etc/GMT-12', 'UTC+12:00'),
                    ('Pacific/Chatham', 'UTC+12:45'),
                    ('Etc/GMT-13', 'UTC+13:00'),
                    ('Etc/GMT-14', 'UTC+14:00'),
                ],
                default='America/Chicago',
                max_length=19,
                verbose_name='UTC time zone',
            ),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activate_timezone',
            field=models.BooleanField(
                default=True,
                verbose_name='Activate this time zone',
            ),
        ),
        migrations.RunPython(set_central_timezone, migrations.RunPython.noop),
    ]
