# Generated by Django 4.2.14 on 2024-07-30 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0010_cart_center4_cart_center5_alter_cart_center1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='centerreview',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
