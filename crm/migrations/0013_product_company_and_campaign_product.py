from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0012_campaign_models'),
    ]

    operations = [
        # Add FoodFight bookkeeping fields to Product
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='products', to='crm.company',
                help_text='Brand or supplier company that provides this product'
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(
                blank=True, max_length=100, null=True,
                help_text="Brand's internal SKU or item code"
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_cost',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True,
                help_text='What FoodFight pays per unit'
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_retail_value',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True,
                help_text='Retail / redemption value per unit (for reporting)'
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='billing_type',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                choices=[
                    ('brand_funded', 'Brand Funded'),
                    ('venue_funded', 'Venue Funded'),
                    ('foodfight_funded', 'FoodFight Funded'),
                    ('split', 'Split'),
                ],
                help_text='Who pays for this product'
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='invoice_notes',
            field=models.TextField(blank=True, null=True),
        ),
        # CampaignProduct model
        migrations.CreateModel(
            name='CampaignProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('units_allocated', models.PositiveIntegerField(default=0)),
                ('units_redeemed', models.PositiveIntegerField(default=0)),
                ('units_invoiced', models.PositiveIntegerField(default=0)),
                ('unit_cost_override', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unit_retail_override', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('billed_to', models.CharField(
                    blank=True, max_length=20, null=True,
                    choices=[
                        ('brand', 'Brand'), ('venue', 'Venue'),
                        ('foodfight', 'FoodFight'), ('split', 'Split'),
                    ]
                )),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('invoice_status', models.CharField(
                    blank=True, max_length=20, null=True, default='pending',
                    choices=[
                        ('pending', 'Pending'), ('sent', 'Sent'),
                        ('paid', 'Paid'), ('disputed', 'Disputed'), ('void', 'Void'),
                    ]
                )),
                ('invoice_notes', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='campaign_products', to='crm.campaign'
                )),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='campaign_products', to='crm.product'
                )),
                ('department', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='auth.group'
                )),
                ('owner', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaignproduct_owner_related',
                    to=settings.AUTH_USER_MODEL
                )),
                ('modified_by', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='crm_campaignproduct_modified_by_related',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'Campaign Product',
                'verbose_name_plural': 'Campaign Products',
                'unique_together': {('campaign', 'product')},
            },
        ),
    ]
