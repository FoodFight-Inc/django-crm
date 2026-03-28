from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0005_userprofile_timezone_defaults'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrmUser',
            fields=[],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
    ]
