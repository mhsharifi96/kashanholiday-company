from django.db import models
from decimal import Decimal
from tours.models import Tour
from accounts.models import BasicUser
from django.db.models.signals import pre_save, post_save, post_delete
# Create your models here.


class CartItem(models.Model):
    cart = models.ForeignKey("Cart")
    item = models.ForeignKey(Tour)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item.name


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = instance.quantity
    if qty >= 1:
        price = instance.item.get_price
        line_item_total = Decimal(qty) * Decimal(price)
        instance.line_item_total = line_item_total


pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)


def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()


post_save.connect(cart_item_post_save_receiver, sender=CartItem)
post_delete.connect(cart_item_post_save_receiver, sender=CartItem)


class Cart(models.Model):
    user = models.ForeignKey(BasicUser, on_delete=models.PROTECT)
    items = models.ManyToManyField(Tour, through=CartItem)
    timestamp = models.DateTimeField(auto_now_add=True, )
    subtotal = models.DecimalField(max_digits=50, default=100.00, verbose_name=u'مجموع', decimal_places=2)\


    class Meta:
        verbose_name = u'سبد خرید'
        verbose_name_plural = u'سبدهای خرید'

    def __str__(self):
        return str(self.id)

    def update_subtotal(self):
        print("Updating...")
        subtotal = 0
        items = self.cartitem_set.all()
        for item in items:
            subtotal += item.line_item_total
        self.subtotal = "%.2f".format(subtotal)
        self.save()




