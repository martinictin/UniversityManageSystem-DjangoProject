# Generated by Django 4.0.4 on 2022-06-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SustavZaUpisStudenata', '0004_remove_predmeti_status_alter_upisi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upisi',
            name='Status',
            field=models.CharField(choices=[('Upisan', 'Upisan'), ('Polozen', 'Polozen'), ('Izgubio potpis', 'Izgubio potpis'), ('Nije upisan', 'Nije upisan')], default='Upisan', max_length=15),
        ),
    ]