# Generated by Django 4.2.2 on 2023-06-13 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Informed', 'Not Informed')], default='Not Informed', max_length=20)),
                ('group_field_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='groups.group')),
            ],
        ),
    ]
