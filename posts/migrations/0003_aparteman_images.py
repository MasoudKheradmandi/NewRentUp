# Generated by Django 4.0.6 on 2022-09-03 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_aparteman_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='aparteman_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.aparteman')),
            ],
        ),
    ]
