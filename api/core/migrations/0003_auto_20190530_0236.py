# Generated by Django 2.2.1 on 2019-05-30 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190530_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to='core.Reporter'),
        ),
    ]
