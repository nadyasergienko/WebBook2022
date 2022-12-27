# Generated by Django 3.2.16 on 2022-12-26 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ('inv_nom',), 'verbose_name': 'Экземпляр книги', 'verbose_name_plural': 'Экземпляры книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('name',), 'verbose_name': 'Язык', 'verbose_name_plural': 'Языки'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('name',), 'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Избранные книги')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]