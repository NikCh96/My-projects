# Generated by Django 4.1.3 on 2022-12-10 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0011_categoriesheader_categoriesleft_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoriesheader',
        ),
        migrations.DeleteModel(
            name='Categoriesleft',
        ),
        migrations.AlterField(
            model_name='location',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.cities'),
        ),
    ]
