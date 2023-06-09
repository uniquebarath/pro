# Generated by Django 4.2 on 2023-05-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=55)),
                ('email', models.CharField(default='', max_length=77)),
                ('number', models.CharField(default='', max_length=70)),
                ('place', models.CharField(default='', max_length=50)),
                ('college', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='college',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.CharField(default='', max_length=77),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='product',
            name='number',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='product',
            name='place',
            field=models.CharField(default='', max_length=50),
        ),
    ]
