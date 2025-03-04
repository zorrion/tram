# Generated by Django 3.2.6 on 2021-12-08 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0008_attackgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adversary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tram.report')),
            ],
        ),
        migrations.CreateModel(
            name='AdversaryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('adversary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tram.adversary')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tram.report')),
            ],
        ),
    ]
