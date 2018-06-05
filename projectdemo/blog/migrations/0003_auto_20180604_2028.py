# Generated by Django 2.0.5 on 2018-06-04 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_aboutauthor_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutAuthor',
            new_name='About',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Meus Posts'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]