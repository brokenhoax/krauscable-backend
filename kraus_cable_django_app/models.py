from django.db import models


class Subscription(models.Model):
    description = models.TextField()
    group = models.CharField(max_length=32)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Customer(models.Model):
    customer_id = models.UUIDField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)
    street_addr1 = models.CharField(max_length=255)
    street_addr2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=32)
    balance_due = models.DecimalField(max_digits=8, decimal_places=2)


class TransactionHistory(models.Model):
    customer_id = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
    )
    transaction_date = models.DateTimeField(null=False)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    balance_due = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.CharFIeld(max_length=255)
