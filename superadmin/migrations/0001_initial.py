# Generated by Django 4.0.1 on 2022-01-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('roll_num', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('students', models.ManyToManyField(related_name='student_teacher', to='superadmin.Student')),
            ],
        ),
    ]
