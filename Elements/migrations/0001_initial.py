# Generated by Django 3.2.19 on 2023-10-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wire_spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wire_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cross_section', models.DecimalField(decimal_places=1, max_digits=3)),
                ('shape', models.CharField(max_length=15)),
                ('Width_to_thickness_ratio', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Radius_of_Chamfer', models.DecimalField(decimal_places=2, max_digits=3)),
                ('material', models.CharField(default='copper', max_length=15)),
                ('temperature_coefficient', models.DecimalField(decimal_places=5, max_digits=6)),
                ('ambient_temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('resistance', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('dissipation_area', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('surface_area', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('conductor_weight', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('specific_heat', models.DecimalField(decimal_places=3, default=None, max_digits=5)),
                ('applied_source', models.CharField(max_length=15)),
                ('source_type', models.CharField(max_length=15)),
                ('peak_source_value', models.DecimalField(decimal_places=1, max_digits=4)),
                ('period_of_source_connection', models.DecimalField(decimal_places=2, max_digits=4)),
                ('step', models.DecimalField(decimal_places=0, max_digits=1)),
                ('frequency', models.DecimalField(decimal_places=1, max_digits=3)),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=4)),
                ('internal_Energy', models.DecimalField(decimal_places=1, max_digits=4)),
                ('hot_Resistance', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]