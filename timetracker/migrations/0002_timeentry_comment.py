from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='comment',
            field=models.TextField(default='', verbose_name='optionnal comment'),
        ),
    ]
