from django.db import models

# Create your models here.
class PiesDev(models.Model):
    brand_aaia_id = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255, null=True)
    sub_brand_aaia_id = models.CharField(max_length=255, null=True, blank=True)
    sub_brand_name = models.CharField(max_length=255, null=True, blank=True)
    part_type_name = models.CharField(max_length=255)
    brand_owner = models.CharField(max_length=255, null=True)
    brand_owner_name = models.CharField(max_length=255, null=True)
    part_number = models.CharField(max_length=255)
    aces_applications = models.TextField(null=True, blank=True)
    piesID = models.IntegerField(primary_key=True)
    brand_id = models.CharField(max_length=255, null=True)
    bu_id = models.CharField(max_length=255)
    BusinessUnit = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    ProductLine = models.CharField(max_length=255)

    class Meta:
        db_table = 'pies_dev'
        managed = False
        app_label = 'api_server'


