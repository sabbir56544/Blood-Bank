# Generated by Django 3.1.1 on 2021-05-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210530_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorregister',
            name='near_hospital',
            field=models.CharField(choices=[('Khulna City Medical', 'Khulna City Medical'), ('Khulna Medical College Hospital', 'Khulna Medical College Hospital'), ('Khulna Sadar Hospital', 'Khulna Sadar Hospital'), ('Islami Bank Hospital', 'Islami Bank Hospital'), ('SANDHANI DONOR CLUB KHULNA', 'SANDHANI DONOR CLUB KHULNA'), ('Khulna Healthcare Hospital', 'Khulna Healthcare Hospital'), ('Surokkha Hospital & Diagnostic', 'Surokkha Hospital & Diagnostic')], default='Khulna Medical College Hospital', max_length=100),
        ),
    ]
