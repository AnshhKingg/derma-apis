# Generated by Django 3.2 on 2022-04-22 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('phoneno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dermacupid.user')),
                ('occupation', models.CharField(blank=True, max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=10, null=True)),
                ('skin_condition', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=10, null=True)),
                ('highest_education', models.CharField(blank=True, max_length=10, null=True)),
                ('education_field', models.CharField(blank=True, max_length=10, null=True)),
                ('profession', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_picture_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_picture_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_picture_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_picture_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_picture_6', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
