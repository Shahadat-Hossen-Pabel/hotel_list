# Generated by Django 4.0.4 on 2022-05-07 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_remove_task_complete_alter_task_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.task')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
