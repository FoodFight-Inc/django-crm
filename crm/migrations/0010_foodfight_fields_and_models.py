from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('crm', '0009_request_case'),
    ]

    operations = [
        # Lead fields
        migrations.AddField(
            model_name='lead',
            name='lead_type',
            field=models.CharField(
                blank=True, max_length=50, null=True,
                choices=[
                    ('venue', 'Venue'), ('venue_group', 'Venue Group'),
                    ('brand', 'Brand'), ('distributor', 'Distributor'),
                    ('agency', 'Agency'), ('campus_partner', 'Campus Partner'),
                    ('influencer', 'Influencer'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_subtype',
            field=models.CharField(
                blank=True, max_length=50, null=True,
                choices=[
                    ('single_venue', 'Single Venue'), ('multi_unit', 'Multi-Unit Operator'),
                    ('chain', 'Chain'), ('hotel_bar', 'Hotel Bar'),
                    ('sports_bar', 'Sports Bar'), ('alumni_bar', 'Alumni Bar'),
                    ('restaurant_group', 'Restaurant Group'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='lead', name='market',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='state_code',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='sports_affiliations',
            field=models.CharField(
                blank=True, max_length=255, null=True,
                help_text='Comma-separated: Bears, Cubs, Michigan, etc.'
            ),
        ),
        migrations.AddField(
            model_name='lead', name='estimated_location_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='estimated_campaign_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='activation_interest',
            field=models.CharField(
                blank=True, max_length=255, null=True,
                help_text='Comma-separated: sampling, watch parties, QR, etc.'
            ),
        ),
        migrations.AddField(
            model_name='lead', name='compliance_complexity',
            field=models.CharField(
                blank=True, max_length=10, null=True,
                choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
            ),
        ),
        migrations.AddField(
            model_name='lead', name='next_best_action',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='warm_intro_source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead', name='foodfight_fit_score',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True,
                help_text="1\u201310 fit score for FoodFight's model"
            ),
        ),
        # Company fields
        migrations.AddField(
            model_name='company', name='account_type',
            field=models.CharField(
                blank=True, max_length=50, null=True,
                choices=[
                    ('venue', 'Venue'), ('venue_group', 'Venue Group'),
                    ('brand', 'Brand'), ('distributor', 'Distributor'),
                    ('agency', 'Agency'), ('university_group', 'University / Alumni Group'),
                    ('creator_partner', 'Creator Partner'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='company', name='partner_status',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('prospect', 'Prospect'), ('pilot', 'Pilot'), ('active', 'Active'),
                    ('paused', 'Paused'), ('churned', 'Churned'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='company', name='market',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company', name='territories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company', name='location_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company', name='primary_revenue_motion',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('platform_fee', 'Platform Fee'), ('sponsorship', 'Sponsorship'),
                    ('rev_share', 'Rev Share'), ('hybrid', 'Hybrid'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='company', name='serves_alcohol',
            field=models.BooleanField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company', name='has_food_program',
            field=models.BooleanField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company', name='pos_system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company', name='jukebox_system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company', name='contract_status',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('none', 'None'), ('draft', 'Draft'), ('sent', 'Sent'),
                    ('signed', 'Signed'), ('expired', 'Expired'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='company', name='renewal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company', name='strategic_priority_tier',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, help_text='1 = highest priority'
            ),
        ),
        migrations.AddField(
            model_name='company', name='internal_owner_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company', name='expansion_readiness_score',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, help_text='1\u201310'
            ),
        ),
        # Contact fields
        migrations.AddField(
            model_name='contact', name='contact_role',
            field=models.CharField(
                blank=True, max_length=30, null=True,
                choices=[
                    ('owner', 'Owner'), ('gm', 'General Manager'),
                    ('beverage_manager', 'Beverage Manager'),
                    ('marketing_manager', 'Marketing Manager'),
                    ('brand_manager', 'Brand Manager'),
                    ('field_marketer', 'Field Marketer'),
                    ('distributor_rep', 'Distributor Rep'),
                    ('agency_lead', 'Agency Lead'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='contact', name='stakeholder_type',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('champion', 'Champion'), ('influencer', 'Influencer'),
                    ('approver', 'Approver'), ('signer', 'Signer'), ('blocker', 'Blocker'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='contact', name='decision_power_score',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, help_text='1\u201310'
            ),
        ),
        migrations.AddField(
            model_name='contact', name='preferred_channel',
            field=models.CharField(
                blank=True, max_length=10, null=True,
                choices=[('text', 'Text'), ('email', 'Email'), ('phone', 'Phone')]
            ),
        ),
        migrations.AddField(
            model_name='contact', name='relationship_strength',
            field=models.CharField(
                blank=True, max_length=10, null=True,
                choices=[('weak', 'Weak'), ('neutral', 'Neutral'), ('strong', 'Strong')]
            ),
        ),
        migrations.AddField(
            model_name='contact', name='favorite_teams',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact', name='last_meeting_date',
            field=models.DateField(blank=True, null=True),
        ),
        # Deal fields
        migrations.AddField(
            model_name='deal', name='opportunity_category',
            field=models.CharField(
                blank=True, max_length=30, null=True,
                choices=[
                    ('venue_subscription', 'Venue Subscription'),
                    ('brand_campaign', 'Brand Campaign'), ('pilot', 'Pilot'),
                    ('multi_market_rollout', 'Multi-Market Rollout'),
                    ('campus_activation', 'Campus Activation'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='deal', name='campaign_type',
            field=models.CharField(
                blank=True, max_length=30, null=True,
                choices=[
                    ('nfl', 'NFL'), ('cfb', 'College Football'),
                    ('march_madness', 'March Madness'), ('ufc', 'UFC'),
                    ('mlb', 'MLB'), ('opening_day', 'Opening Day'),
                    ('world_cup', 'World Cup'), ('always_on', 'Always On'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='deal', name='target_launch_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='campaign_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='campaign_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='states_in_scope',
            field=models.CharField(
                blank=True, max_length=255, null=True,
                help_text='Comma-separated state codes'
            ),
        ),
        migrations.AddField(
            model_name='deal', name='locations_in_scope',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_signups',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_entries',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_redemptions',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_sponsorship_revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_platform_revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expected_margin',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True,
                help_text='Margin %'
            ),
        ),
        migrations.AddField(
            model_name='deal', name='deal_compliance_status',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('not_started', 'Not Started'), ('in_review', 'In Review'),
                    ('approved', 'Approved'), ('blocked', 'Blocked'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='deal', name='loss_reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deal', name='expansion_path',
            field=models.TextField(blank=True, null=True),
        ),
        # New models
        migrations.CreateModel(
            name='VenueProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_owner_related',
                    to='auth.user'
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_modified_by_related',
                    to='auth.user'
                )),
                ('company', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='venue_profile', to='crm.company'
                )),
                ('venue_type', models.CharField(
                    blank=True, max_length=30, null=True,
                    choices=[
                        ('sports_bar', 'Sports Bar'), ('restaurant', 'Restaurant'),
                        ('hotel_bar', 'Hotel Bar'), ('alumni_bar', 'Alumni Bar'),
                        ('campus', 'Campus'), ('entertainment', 'Entertainment Venue'),
                    ]
                )),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('avg_game_day_traffic', models.PositiveIntegerField(blank=True, null=True)),
                ('avg_weekend_traffic', models.PositiveIntegerField(blank=True, null=True)),
                ('team_affiliations', models.CharField(blank=True, max_length=255, null=True)),
                ('supports_sampling', models.BooleanField(blank=True, null=True)),
                ('has_qr_placement', models.BooleanField(blank=True, null=True)),
                ('has_tv_audio', models.BooleanField(blank=True, null=True)),
                ('has_patio', models.BooleanField(blank=True, null=True)),
                ('kitchen_open_late', models.BooleanField(blank=True, null=True)),
                ('staff_incentive_enabled', models.BooleanField(blank=True, null=True)),
                ('launch_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('not_launched', 'Not Launched'), ('in_setup', 'In Setup'),
                        ('live', 'Live'), ('paused', 'Paused'),
                    ]
                )),
            ],
            options={'verbose_name': 'Venue Profile', 'verbose_name_plural': 'Venue Profiles'},
        ),
        migrations.CreateModel(
            name='BrandProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_owner_related',
                    to='auth.user'
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_modified_by_related',
                    to='auth.user'
                )),
                ('company', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='brand_profile', to='crm.company'
                )),
                ('brand_category', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('beer', 'Beer'), ('spirits', 'Spirits'), ('rtd', 'RTD'),
                        ('seltzer', 'Seltzer'), ('na', 'Non-Alcoholic'),
                    ]
                )),
                ('portfolio_names', models.CharField(blank=True, max_length=255, null=True)),
                ('priority_markets', models.CharField(blank=True, max_length=255, null=True)),
                ('distributor_network_notes', models.TextField(blank=True, null=True)),
                ('consumer_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('trade_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('reporting_requirements', models.TextField(blank=True, null=True)),
                ('legal_constraints_notes', models.TextField(blank=True, null=True)),
            ],
            options={'verbose_name': 'Brand Profile', 'verbose_name_plural': 'Brand Profiles'},
        ),
        migrations.CreateModel(
            name='ActivationCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_owner_related',
                    to='auth.user'
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_modified_by_related',
                    to='auth.user'
                )),
                ('deal', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='campaigns', to='crm.deal'
                )),
                ('name', models.CharField(max_length=255)),
                ('campaign_type', models.CharField(
                    blank=True, max_length=30, null=True,
                    choices=[
                        ('nfl', 'NFL'), ('cfb', 'College Football'),
                        ('march_madness', 'March Madness'), ('ufc', 'UFC'),
                        ('mlb', 'MLB'), ('opening_day', 'Opening Day'),
                        ('world_cup', 'World Cup'), ('always_on', 'Always On'),
                    ]
                )),
                ('sports_moment', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_type', models.CharField(
                    blank=True, max_length=30, null=True,
                    choices=[
                        ('free_sample', 'Free Sample'), ('discount', 'Discount'),
                        ('merch', 'Merch'), ('bracket_promo', 'Bracket Promo'),
                        ('trivia', 'Trivia'), ('prediction', 'Prediction'),
                    ]
                )),
                ('cta_type', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('sponsor_account', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='sponsored_campaigns', to='crm.company'
                )),
                ('venue_accounts', models.ManyToManyField(
                    blank=True, related_name='venue_campaigns', to='crm.company'
                )),
                ('creative_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('not_started', 'Not Started'), ('in_progress', 'In Progress'),
                        ('approved', 'Approved'), ('live', 'Live'),
                    ]
                )),
                ('compliance_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('not_started', 'Not Started'), ('in_review', 'In Review'),
                        ('approved', 'Approved'), ('blocked', 'Blocked'),
                    ]
                )),
                ('launch_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('not_launched', 'Not Launched'), ('in_setup', 'In Setup'),
                        ('live', 'Live'), ('complete', 'Complete'),
                    ]
                )),
                ('reporting_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('pending', 'Pending'), ('in_progress', 'In Progress'),
                        ('complete', 'Complete'),
                    ]
                )),
            ],
            options={'verbose_name': 'Activation Campaign', 'verbose_name_plural': 'Activation Campaigns'},
        ),
        migrations.CreateModel(
            name='ComplianceProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_owner_related',
                    to='auth.user'
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_modified_by_related',
                    to='auth.user'
                )),
                ('deal', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='compliance_profiles', to='crm.deal'
                )),
                ('campaign', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='compliance_profiles', to='crm.activationcampaign'
                )),
                ('state_code', models.CharField(max_length=2)),
                ('promotion_type', models.CharField(blank=True, max_length=100, null=True)),
                ('full_size_allowed', models.BooleanField(blank=True, null=True)),
                ('sample_only', models.BooleanField(blank=True, null=True)),
                ('brand_funded_only', models.BooleanField(blank=True, null=True)),
                ('venue_funded_allowed', models.BooleanField(blank=True, null=True)),
                ('max_value_limit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('counsel_review_required', models.BooleanField(default=False)),
                ('counsel_status', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('not_started', 'Not Started'), ('in_review', 'In Review'),
                        ('approved', 'Approved'), ('rejected', 'Rejected'),
                    ]
                )),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={'verbose_name': 'Compliance Profile', 'verbose_name_plural': 'Compliance Profiles'},
        ),
        migrations.CreateModel(
            name='PerformanceSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_owner_related',
                    to='auth.user'
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='%(app_label)s_%(class)s_modified_by_related',
                    to='auth.user'
                )),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='snapshots', to='crm.activationcampaign'
                )),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('signups', models.PositiveIntegerField(default=0)),
                ('entries', models.PositiveIntegerField(default=0)),
                ('redemptions', models.PositiveIntegerField(default=0)),
                ('staff_referrals', models.PositiveIntegerField(default=0)),
                ('estimated_incremental_sales', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('estimated_impressions', models.PositiveIntegerField(blank=True, null=True)),
                ('repeat_user_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=5, null=True,
                    help_text='Percentage'
                )),
                ('venue_roi_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Performance Snapshot',
                'verbose_name_plural': 'Performance Snapshots',
                'ordering': ['-period_start'],
            },
        ),
    ]
