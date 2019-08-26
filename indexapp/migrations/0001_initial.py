# Generated by Django 2.0.6 on 2019-07-24 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCategory',
            fields=[
                ('category_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=20, null=True)),
                ('book_counts', models.CharField(blank=True, max_length=10, null=True)),
                ('category_pid', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_category',
            },
        ),
        migrations.CreateModel(
            name='DOrderiterm',
            fields=[
                ('shop_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shop_bookid', models.CharField(blank=True, max_length=20, null=True)),
                ('shop_ordid', models.CharField(blank=True, max_length=20, null=True)),
                ('shop_num', models.CharField(blank=True, max_length=20, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_orderiterm',
            },
        ),
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('detail_address', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('telphone', models.CharField(blank=True, max_length=20, null=True)),
                ('addr_mobile', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(blank=True, max_length=128, null=True)),
                ('book_author', models.CharField(blank=True, max_length=64, null=True)),
                ('book_publish', models.CharField(blank=True, max_length=128, null=True)),
                ('publish_time', models.DateField(blank=True, null=True)),
                ('revision', models.IntegerField(blank=True, null=True)),
                ('book_isbn', models.CharField(blank=True, max_length=64, null=True)),
                ('word_count', models.CharField(blank=True, max_length=64, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('open_type', models.CharField(blank=True, max_length=20, null=True)),
                ('book_paper', models.CharField(blank=True, max_length=64, null=True)),
                ('book_wrapper', models.CharField(blank=True, max_length=64, null=True)),
                ('book_category', models.CharField(blank=True, max_length=11, null=True)),
                ('book_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('book_dprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('editor_recommendation', models.CharField(blank=True, max_length=2000, null=True)),
                ('content_introduction', models.CharField(blank=True, max_length=2000, null=True)),
                ('author_introduction', models.CharField(blank=True, max_length=2000, null=True)),
                ('menu', models.CharField(blank=True, max_length=2000, null=True)),
                ('media_review', models.CharField(blank=True, max_length=2000, null=True)),
                ('digest_image_path', models.CharField(blank=True, max_length=2000, null=True)),
                ('product_image_path', models.CharField(blank=True, max_length=2000, null=True)),
                ('series_name', models.CharField(blank=True, max_length=128, null=True)),
                ('printing_time', models.DateField(blank=True, null=True)),
                ('impression', models.CharField(blank=True, max_length=64, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('shelves_date', models.DateField(blank=True, null=True)),
                ('customer_score', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('book_status', models.CharField(blank=True, max_length=10, null=True)),
                ('sales', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='TShopcar',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_field', models.IntegerField(blank=True, db_column='book_', null=True)),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('counts', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_shopcar',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(blank=True, max_length=50, null=True)),
                ('user_password', models.CharField(blank=True, max_length=20, null=True)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('user_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='indexapp.TAddress')),
                ('num', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('order_addrid', models.CharField(blank=True, max_length=20, null=True)),
                ('order_uid', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_order',
            },
        ),
    ]