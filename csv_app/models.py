from django.db import models
from django.db.models import Manager
from django.db.models.query import QuerySet


class CaseInsensitiveQuerySet(QuerySet):
  def _filter_or_exclude(self, mapper, *args, **kwargs):
  # 'name' is a field in your Model whose lookups you want case-insensitive by default
    if 'sku' in kwargs:
      kwargs['sku__iexact'] = kwargs['sku']
      del kwargs['sku']
    return super(CaseInsensitiveQuerySet, self)._filter_or_exclude(mapper, *args, **kwargs)
# custom manager that overrides the initial query set
class BrandManager(Manager):
  def get_query_set(self):
    return CaseInsensitiveQuerySet(self.model)
# and the model itself

class Product(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name= models.CharField(max_length=50)
    sku =models.CharField(max_length=200, unique=True, db_index=True)
    # objects = BrandManager()
    description= models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='active')

    def __str__(self):
        return self.name
