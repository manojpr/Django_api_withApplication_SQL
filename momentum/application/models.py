from django.db import models

# Create your models here.
class DIM_BU(models.Model):
    bu_id = models.CharField(max_length=255, primary_key=True)
    BusinessUnit = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    ProductLine = models.CharField(max_length=255)
    part_type_name = models.CharField(max_length=255)

    class Meta:
        managed = False  # This model is not managed by Django migrations
        db_table = 'DIM_BU'  # Specify the database table name

    def __str__(self):
        return self.bu_id  # Display the bu_id in Django admin and shell

class DIMBrand(models.Model):
    sub_brand_aaia_id = models.CharField(max_length=100)
    subbrandname = models.CharField(max_length=255)
    brandid = models.CharField(max_length=100)
    brandname = models.CharField(max_length=255)
    brandownerid = models.CharField(max_length=100)
    brandownername = models.CharField(max_length=255)
    brand_id = models.CharField(max_length=100 , primary_key=True)

    class Meta:
        db_table = 'DIM_brand'
        managed = False  # Set to False if the table is managed outside of Django, e.g., by another application or manually

    def __str__(self):
        return self.subbrandname