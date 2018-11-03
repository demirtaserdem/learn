# Generated by Django 2.0.3 on 2018-11-03 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20181102_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum')),
                ('comment_date', models.DateField(auto_now_add=True, verbose_name='Yorum Tarihi')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Makale'),
        ),
    ]
