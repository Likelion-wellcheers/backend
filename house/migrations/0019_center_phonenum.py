# Generated by Django 4.2.14 on 2024-08-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("house", "0018_alter_cart_center1_alter_cart_center2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="center",
            name="phonenum",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="전화번호"
            ),
        ),
    ]
