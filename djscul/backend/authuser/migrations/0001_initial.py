# Generated by Django 4.0.1 on 2022-01-12 18:39

import backend.authuser.models.user
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid_key', models.CharField(db_index=True, default=backend.authuser.models.user.generate_uuid, max_length=100)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'none'), (2, 'student'), (3, 'parent'), (4, 'teacher')], default=1)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+993 131 99999'. Up to 15 digits allowed.", regex='^(?:\\+993)?[ ]?(?:\\([1-5]?[1-5]{2,3}\\)[ .-]?[0-9]{1}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|[1-5]?[1-5]{2,3}[ .-]?[0-9]{1}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|[1-5]?[1-5]{2,3}[0-9]{5,6})$')])),
                ('mobile', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+993 61 999999'. Up to 15 digits allowed.", regex='^(?:\\+993)?[ ]?(?:\\(6[1-5]?\\)[ .-]?[0-9]{2}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|6[1-5]?[ .-]?[0-9]{2}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|6[1-5]?[0-9]{6})$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'none'), (2, 'student'), (3, 'parent'), (4, 'teacher')], default=1, verbose_name='User')),
                ('att_name', models.CharField(help_text='Required', max_length=255, verbose_name='Name')),
                ('att_type', models.PositiveSmallIntegerField(choices=[(0, 'Int'), (1, 'String'), (2, 'Date'), (5, 'Static list'), (6, 'Relation')], default=0, verbose_name='Type')),
                ('att_len', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Length')),
                ('att_info', models.CharField(blank=True, help_text='Set model name if type is relation', max_length=25, verbose_name='Info')),
            ],
            options={
                'verbose_name': 'User Attribute',
                'verbose_name_plural': 'User Attributes',
                'db_table': 'auth_user_attribute',
            },
        ),
        migrations.CreateModel(
            name='UserAttributeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att_value', models.CharField(help_text='User Attribute Value', max_length=255, verbose_name='Attribute Value')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('attrib_fk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authuser.userattribute', verbose_name='Attribute name')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields_data', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Attribute value',
                'verbose_name_plural': 'User Attribute values',
                'db_table': 'auth_ud_value',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authuser.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authuser.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authuser.user',),
        ),
    ]
