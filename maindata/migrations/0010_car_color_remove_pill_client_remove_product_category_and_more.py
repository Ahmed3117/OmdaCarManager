# Generated by Django 4.2.4 on 2024-01-17 17:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0009_alter_paid_date_added_alter_pill_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture_year', models.CharField(blank=True, max_length=10, null=True, verbose_name=' سنة الصنع')),
                ('government', models.CharField(blank=True, choices=[('1', 'القاهرة'), ('2', 'الغربية'), ('3', 'كفر الشيخ'), ('4', 'المنوفية'), ('5', 'الدقهلية'), ('6', 'الإسكندرية'), ('7', 'البحيرة'), ('8', 'الإسماعيلية'), ('9', 'الجيزة'), ('10', 'السويس'), ('11', 'الشرقية'), ('12', 'القليوبية'), ('13', 'بني سويف'), ('14', 'الفيوم'), ('15', 'دمياط'), ('16', 'البحر الأحمر'), ('17', 'بورسعيد'), ('18', 'أسوان'), ('19', 'أسيوط'), ('20', 'الأقصر'), ('21', 'سوهاج'), ('22', 'قنا'), ('23', 'مطروح'), ('24', 'المنيا'), ('25', 'الوادي الجديد'), ('26', 'جنوب سيناء'), ('27', 'شمال سيناء')], default='1', max_length=50, null=True, verbose_name='  المحافظة ')),
                ('traffic', models.CharField(blank=True, max_length=200, null=True, verbose_name='  المرور ')),
                ('gawap_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='  نوع الجواب ')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name=' تاريخ دخول المعرض')),
                ('native_price', models.FloatField(blank=True, default=0, null=True, verbose_name='السعر الشراء ')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='  ملاحظات ')),
                ('garunty', models.CharField(blank=True, choices=[('1', 'موجود'), ('2', 'غير موجود')], default='1', max_length=50, null=True, verbose_name=' الضمان ')),
                ('garunty_file', models.FileField(blank=True, null=True, upload_to='garunty_files/', verbose_name='  صورة من الضمان')),
                ('code', models.CharField(blank=True, editable=False, max_length=12, null=True, verbose_name='كود السيارة')),
            ],
            options={
                'verbose_name': '   سيارة',
                'verbose_name_plural': '  السيارات ',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='اللون')),
            ],
            options={
                'verbose_name': '    لون',
                'verbose_name_plural': 'الالوان ',
            },
        ),
        migrations.RemoveField(
            model_name='pill',
            name='client',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '   نوع سيارة', 'verbose_name_plural': '   انواع السيارات '},
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='added_value_for_deposite',
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='pill',
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='selloperation',
            name='sell_type',
        ),
        migrations.AddField(
            model_name='client',
            name='selloperation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maindata.selloperation', verbose_name=' عملية بيع'),
        ),
        migrations.AddField(
            model_name='selloperation',
            name='paid',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name=' المدفوع'),
        ),
        migrations.AddField(
            model_name='selloperation',
            name='sell_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 17, 19, 40, 25, 894652), null=True, verbose_name=' تاريخ الخروج'),
        ),
        migrations.AddField(
            model_name='selloperation',
            name='sell_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name=' سعر البيع '),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=' نوع السيارة'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=' اسم المعاق'),
        ),
        migrations.DeleteModel(
            name='Paid',
        ),
        migrations.DeleteModel(
            name='Pill',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maindata.category', verbose_name=' نوع السيارة'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maindata.color', verbose_name='اللون'),
        ),
        migrations.AddField(
            model_name='selloperation',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maindata.car', verbose_name='  السيارة'),
        ),
    ]
