from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0011_foodfight_stages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(
                    max_length=20, default='draft',
                    choices=[
                        ('draft', 'Draft'), ('scheduled', 'Scheduled'),
                        ('active', 'Active'), ('paused', 'Paused'),
                        ('cancelled', 'Cancelled'), ('completed', 'Completed'),
                    ]
                )),
                ('notes', models.TextField(blank=True, null=True)),
                ('offer_type', models.CharField(
                    max_length=20, blank=True, null=True,
                    choices=[
                        ('beer', 'Beer'), ('spirits', 'Spirits'), ('shot', 'Shot'),
                        ('food', 'Food'), ('prize', 'Prize'),
                        ('coupon', 'Coupon / Discount'), ('merch', 'Merch'), ('other', 'Other'),
                    ]
                )),
                ('offer_description', models.CharField(max_length=255, blank=True, null=True)),
                ('offer_value', models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('league', models.CharField(
                    max_length=20, blank=True, null=True,
                    choices=[
                        ('nfl', 'NFL'), ('cfb', 'College Football'), ('nba', 'NBA'),
                        ('mlb', 'MLB'), ('nhl', 'NHL'), ('ufc', 'UFC'),
                        ('soccer', 'Soccer'), ('march_madness', 'March Madness'), ('other', 'Other'),
                    ]
                )),
                ('team', models.CharField(max_length=100, blank=True, null=True)),
                ('game_schedule_type', models.CharField(
                    max_length=30, blank=True, null=True,
                    choices=[
                        ('any', 'Any Game'), ('specific_date', 'Specific Date'),
                        ('monday_night', 'Monday Night Football'), ('super_bowl', 'Super Bowl'),
                        ('march_madness', 'March Madness'), ('opening_day', 'Opening Day'),
                        ('playoffs', 'Playoffs'), ('championship', 'Championship'),
                        ('season', 'Full Season'), ('preseason', 'Preseason'),
                        ('first_half', 'First Half of Season'), ('second_half', 'Second Half of Season'),
                        ('happy_hour', 'Happy Hour'), ('other', 'Other'),
                    ]
                )),
                ('max_global', models.PositiveIntegerField(blank=True, null=True)),
                ('max_per_venue', models.PositiveIntegerField(blank=True, null=True)),
                ('max_per_individual', models.PositiveIntegerField(blank=True, null=True)),
                ('redeemed_count', models.PositiveIntegerField(default=0)),
                ('active_count', models.PositiveIntegerField(default=0)),
                ('invoiced_amount', models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)),
                ('company', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='campaigns', to='crm.company'
                )),
                ('contact', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='campaigns', to='crm.contact'
                )),
                ('deal', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='promo_campaigns', to='crm.deal'
                )),
                ('parent_campaign', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='sub_campaigns', to='crm.campaign'
                )),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaign_owner_related',
                    to=settings.AUTH_USER_MODEL
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaign_modified_by_related',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='CampaignVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('venue_items', models.TextField(blank=True, null=True)),
                ('max_override', models.PositiveIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='campaign_venues', to='crm.campaign'
                )),
                ('venue', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='campaign_venues', to='crm.company'
                )),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaignvenue_owner_related',
                    to=settings.AUTH_USER_MODEL
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaignvenue_modified_by_related',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'Campaign Venue',
                'verbose_name_plural': 'Campaign Venues',
                'unique_together': {('campaign', 'venue')},
            },
        ),
        migrations.CreateModel(
            name='OutcomePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('scope', models.CharField(
                    max_length=30,
                    choices=[
                        ('microtransaction', 'Microtransaction (e.g. Next Score)'),
                        ('game_progression', 'Game Progression (e.g. Q1, Half)'),
                        ('final_outcome', 'Final Outcome (Win / Loss)'),
                    ]
                )),
                ('outcome_type', models.CharField(
                    max_length=30,
                    choices=[
                        ('next_score', 'Next Score'), ('next_td', 'Next Touchdown'),
                        ('next_fg', 'Next Field Goal'), ('q1', 'End of Q1'),
                        ('q2', 'End of Q2'), ('halftime', 'Halftime'),
                        ('q3', 'End of Q3'), ('q4', 'End of Q4 / Final'),
                        ('win', 'Win'), ('loss', 'Loss'),
                        ('any', 'Any Outcome'), ('other', 'Other'),
                    ]
                )),
                ('description', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='outcome_pools', to='crm.campaign'
                )),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_outcomepool_owner_related',
                    to=settings.AUTH_USER_MODEL
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_outcomepool_modified_by_related',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'Outcome Pool',
                'verbose_name_plural': 'Outcome Pools',
            },
        ),
        migrations.CreateModel(
            name='PromoTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('scheduled_for', models.DateTimeField()),
                ('promo_count', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(
                    max_length=20, default='pending',
                    choices=[
                        ('pending', 'Pending'), ('live', 'Live'),
                        ('expired', 'Expired'), ('cancelled', 'Cancelled'),
                    ]
                )),
                ('notes', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='promo_targets', to='crm.campaign'
                )),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_promotarget_owner_related',
                    to=settings.AUTH_USER_MODEL
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_promotarget_modified_by_related',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'Promo Target',
                'verbose_name_plural': 'Promo Targets',
                'ordering': ['scheduled_for'],
            },
        ),
    ]
