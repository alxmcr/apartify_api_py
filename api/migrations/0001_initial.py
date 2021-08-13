# Generated by Django 3.2.6 on 2021-08-13 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('ap_apartment', models.BigAutoField(primary_key=True, serialize=False)),
                ('ap_description', models.TextField(max_length=1000, unique=True, verbose_name='Description')),
                ('ap_floor_number', models.IntegerField(default=0, verbose_name='Floor Number')),
                ('ap_cost_offer', models.CharField(max_length=50, verbose_name='Offer Cost')),
                ('ap_cost_list', models.CharField(max_length=50, verbose_name='List cost')),
                ('ap_is_remodeling', models.BooleanField(verbose_name='Is it remodeling?')),
                ('ap_latitude', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Latitude')),
                ('ap_longitude', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Longitude')),
                ('ap_street_name', models.CharField(default='', max_length=80, verbose_name='Street Name')),
                ('ap_ext_number', models.CharField(default=0, max_length=10, verbose_name='Exterior Number')),
                ('ap_int_number', models.CharField(default=0, max_length=10, verbose_name='Interior Number')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('ci_city', models.BigAutoField(primary_key=True, serialize=False)),
                ('ci_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('ci_abbr', models.CharField(max_length=5, unique=True, verbose_name='Abbreviation')),
                ('ci_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Photo')),
                ('ci_alt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Photo Alternative Text')),
            ],
        ),
        migrations.CreateModel(
            name='CityHall',
            fields=[
                ('ch_city_hall', models.BigAutoField(primary_key=True, serialize=False)),
                ('ch_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('ch_abbr', models.CharField(max_length=5, unique=True, verbose_name='Abbreviation')),
                ('ch_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Photo')),
                ('ch_alt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Photo Alternative Text')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('co_country', models.BigAutoField(primary_key=True, serialize=False)),
                ('co_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('co_abbr', models.CharField(max_length=5, unique=True, verbose_name='Abbreviation')),
                ('co_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Photo')),
                ('co_alt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Photo Alternative Text')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('fe_feature', models.BigAutoField(primary_key=True, serialize=False)),
                ('fe_type', models.CharField(max_length=50, verbose_name='Type')),
                ('fe_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('fe_icon_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Icon')),
                ('fe_icon_color', models.CharField(blank=True, max_length=80, null=True, verbose_name='Color Icon')),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('in_investment', models.BigAutoField(primary_key=True, serialize=False)),
                ('in_type', models.CharField(max_length=30, verbose_name='Type')),
                ('in_name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('in_icon_url', models.CharField(blank=True, max_length=150, verbose_name='URL Icon')),
                ('in_icon_color', models.CharField(blank=True, max_length=80, verbose_name='Color Icon')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('ne_neighborhood', models.BigAutoField(primary_key=True, serialize=False)),
                ('ne_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('ne_abbr', models.CharField(max_length=5, unique=True, verbose_name='Abbreviation')),
                ('ne_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Photo')),
                ('ne_alt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Photo Alternative Text')),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorSpace',
            fields=[
                ('ou_outdoor_space', models.BigAutoField(primary_key=True, serialize=False)),
                ('ou_type', models.CharField(max_length=30, verbose_name='Type')),
                ('ou_name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('ou_icon_url', models.CharField(blank=True, max_length=150, verbose_name='URL Icon')),
                ('ou_icon_color', models.CharField(blank=True, max_length=80, verbose_name='Color Icon')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('st_state', models.BigAutoField(primary_key=True, serialize=False)),
                ('st_name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('st_abbr', models.CharField(max_length=5, unique=True, verbose_name='Abbreviation')),
                ('st_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='URL Photo')),
                ('st_alt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Photo Alternative Text')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('ph_photo', models.BigAutoField(primary_key=True, serialize=False)),
                ('ph_url', models.CharField(max_length=150, verbose_name='URL Photo')),
                ('ph_alt', models.CharField(max_length=80, verbose_name='Photo Alternative Text')),
                ('ap_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Outdoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_value', models.CharField(max_length=10, verbose_name='Value')),
                ('out_is_visible', models.BooleanField(default=True, verbose_name='Is it visible?')),
                ('out_is_card', models.BooleanField(default=True, verbose_name='Is it in a card?')),
                ('ap_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apartment')),
                ('ou_outdoor_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.outdoorspace')),
            ],
        ),
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_value', models.CharField(max_length=10, verbose_name='Value')),
                ('inv_is_visible', models.BooleanField(default=True, verbose_name='Is it visible?')),
                ('inv_is_card', models.BooleanField(default=True, verbose_name='Is it in a card?')),
                ('ap_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apartment')),
                ('in_investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.investment')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('fl_flat', models.BigAutoField(primary_key=True, serialize=False)),
                ('fl_url', models.CharField(max_length=150, verbose_name='URL Flat')),
                ('fl_alt', models.CharField(max_length=80, verbose_name='Flat Alternative Text')),
                ('ap_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Attract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att_value', models.CharField(max_length=10, verbose_name='Value')),
                ('att_is_visible', models.BooleanField(default=True, verbose_name='Is it visible?')),
                ('att_is_card', models.BooleanField(default=True, verbose_name='Is it in a card?')),
                ('ap_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apartment')),
                ('fe_feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.feature')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='ch_city_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cityhall'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='ci_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='co_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='features',
            field=models.ManyToManyField(through='api.Attract', to='api.Feature'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='investments',
            field=models.ManyToManyField(through='api.Invest', to='api.Investment'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='ne_neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.neighborhood'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='outdoor_spaces',
            field=models.ManyToManyField(through='api.Outdoor', to='api.OutdoorSpace'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='st_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state'),
        ),
    ]
