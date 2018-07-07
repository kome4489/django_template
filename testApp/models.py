from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField()

class Category(models.Model):
    rowkey = models.AutoField(db_column='RowKey', primary_key=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='categoryId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categorydetail = models.CharField(db_column='categoryDetail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'