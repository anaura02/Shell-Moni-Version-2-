from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank_balance = models.DecimalField(max_digits=12, decimal_places=2)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.account_type} - {self.customer.first_name}"

class Payee(models.Model):
    payee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)  # deposit/withdrawal
    date = models.DateTimeField(auto_now_add=True)
    payee = models.ForeignKey(Payee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
