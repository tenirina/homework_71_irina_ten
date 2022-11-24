# Generated by Django 4.1.2 on 2022-11-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_birthday_account_count_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(upload_to='avatars', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Man'), ('FEMALE', 'Women')], default='MALE', max_length=10, null=True, verbose_name='Gender'),
        ),
    ]