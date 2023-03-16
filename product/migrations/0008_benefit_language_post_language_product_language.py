# Generated by Django 4.1.7 on 2023-03-15 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_order_canceled_order_confirmed_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefit',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.language'),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.language'),
        ),
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.language'),
        ),
    ]