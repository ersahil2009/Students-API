# Generated by Django 4.0.3 on 2022-03-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=200)),
                ('rollno', models.PositiveIntegerField()),
                ('parents_name', models.CharField(max_length=200)),
                ('mo', models.PositiveBigIntegerField()),
                ('total_subjects', models.PositiveIntegerField()),
                ('results', models.FloatField()),
                ('grd', models.CharField(max_length=10)),
            ],
        ),
    ]
