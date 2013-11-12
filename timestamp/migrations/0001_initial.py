# encoding: utf8
from django.db import models, migrations
import timestamp.models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('created', timestamp.models.DbDateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'TimeStampModel',
        ),
        migrations.RunSQL(
            "ALTER TABLE timestamp_timestampmodel ALTER COLUMN created SET DEFAULT NOW()"
        ),
    ]
