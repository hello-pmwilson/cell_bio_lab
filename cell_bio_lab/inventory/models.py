from django.db import models

# Create your models here.
class item(models.Model):
    item = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()

    def __str__(self):
        return self.item_name

class vendor(models.Model):
    vendor = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.vendor_name

class unit(models.Model):
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.unit

class location(models.Model):
    location = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name   
    
class inventory(models.Model):
    inventory = models.AutoField(primary_key=True)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    unit = models.ForeignKey(unit, on_delete=models.SET("unit(s)"))
    location_name = models.ForeignKey(location, on_delete=models.SET("Lab"))

    def __str__(self):
        return f"{self.inventory} {self.item}"
    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"

class purchase_reference(models.Model):
    purchase_reference = models.AutoField(primary_key=True)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    catalog = models.CharField(max_length=25)
    price = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    unit = models.ForeignKey(unit, on_delete=models.SET("unit(s)"))

    class Meta:
        verbose_name = "Purchase Reference"
        verbose_name_plural = "Purchase References"

status_options = [
('submitted', 'Submitted'),
('approved', 'Approved'),
('pending', 'Pending'),
('requested', 'Requested'),
('ordered', 'Ordered'),
]

class purchase_orders(models.Model):
    po = models.PositiveSmallIntegerField()
    status = models.CharField(15, choices=status_options)

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

class on_order(models.Model):    
    purchase_reference = models.ForeignKey(purchase_reference, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=status_options)
    po = models.ForeignKey(purchase_orders, on_delete=models.CASCADE)
    date = models.DateField(null=True) ##auto_now_add=True

    class Meta:
        verbose_name = "Ordered"
        verbose_name_plural = "Ordered"

class on_request(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    unit = models.ForeignKey(unit, on_delete=models.SET("unit(s)"))
    status = models.CharField(max_length=15, choices=status_options)

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

