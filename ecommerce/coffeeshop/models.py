from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - ₦{self.price} X{self.stock_quantity}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_order_price = models.DecimalField(max_digits=10, decimal_places=2)

    # @property
    # def total_price(self):
    #     total = 0
    #     for item in self.orderitem_set.all():
    #         item_price = item.product.price * item.quantity
    #         total += item_price
    #     return total

    def total_price(self):
        total = 0
        total = sum((item.product.price * item.quantity for item in self.orderitem_set.all()))
        # for item in self.orderitem_set.all():
        #     item_price = item.product.price * item.quantity
        #     total += item_price
        return total

    def __str__(self):
        # return f"{self.customer} - ₦{self.total_price}"
        return f"{self.customer}"
    

    def save(self):
        self.total_order_price = self.total_price()
        super().save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.product} x{self.quantity}"
