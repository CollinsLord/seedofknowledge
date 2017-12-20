# Generated by Django 2.0 on 2017-12-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
            options={
                'ordering': ['subject', 'number'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together={('number', 'subject')},
        ),
    ]