# Generated by Django 2.2.4 on 2019-10-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0002_auto_20191025_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacion', models.CharField(max_length=300)),
                ('resultado', models.TextField(default='')),
                ('color', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Recomendacion',
        ),
    ]
