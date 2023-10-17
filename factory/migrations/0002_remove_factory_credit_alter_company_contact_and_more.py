# Generated by Django 4.2.4 on 2023-10-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("factory", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="factory",
            name="credit",
        ),
        migrations.AlterField(
            model_name="company",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="factory.contacts",
                verbose_name="контакты",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="factory.products",
                verbose_name="продукция",
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="factory.contacts",
                verbose_name="контакты",
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="product",
            field=models.ManyToManyField(
                to="factory.products", verbose_name="продукция"
            ),
        ),
        migrations.AlterField(
            model_name="retail",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="factory.contacts",
                verbose_name="контакты",
            ),
        ),
        migrations.AlterField(
            model_name="retail",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="factory.products",
                verbose_name="продукция",
            ),
        ),
    ]
