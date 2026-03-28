from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_operation_leads_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(
                blank=True, max_length=20, null=True,
                verbose_name='Product category',
                choices=[
                    ('beer', 'Beer'),
                    ('spirits', 'Spirits'),
                    ('wine', 'Wine'),
                    ('shot', 'Shot'),
                    ('food', 'Food'),
                    ('merch', 'Merchandise'),
                    ('coupon', 'Coupon / Discount'),
                    ('prize', 'Prize'),
                    ('experience', 'Experience'),
                    ('digital', 'Digital'),
                    ('other', 'Other'),
                ],
            ),
        ),
    ]
