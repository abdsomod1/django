from django.db import models
from decimal import Decimal
import uuid

# Create your models here.
class ProductCategory(models.TextChoices):
    FASHION = ('FASH', 'Fashion')
    TECHNOLOGY = ('TECH', 'Technology')
    BEAUTY = ('BT', 'Beauty')
    OTHER =('OTHER', 'Other')

class Product(models.Model):
    name = models.CharField(max_length=255, )
    price = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits= 9)
    category = models.CharField(choices=ProductCategory.choices, default=ProductCategory.TECHNOLOGY, max_length=255)
    orderid = models.ForeignKey('order', on_delete=models.SET_NULL,
                                null= True,
                                related_name='Product')
    class Meta:
        ordering = ['-name']
        indexes = [models.Index(
            fields=['id', 'name']
        )]
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category
        }
class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Model.objects.create()
# obj.save()
# obj.delete()
# Model.objects.filter()
# Model.objects.orderby()
# Producs.objects.all().paginate(page=1, per_page=50)

# order = Order.objects.filter_by()
# p = Product.objects.fileter(price__gt=50).first()
# p.order = order
# order.products.add(p)