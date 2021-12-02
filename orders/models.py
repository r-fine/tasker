from django.db import models
from django.conf import settings

from services.models import Service


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    AREA = (
        ('Abdullahpur', 'Abdullahpur'),
        ('Agargaon', 'Agargaon'),
        ('Badda', 'Badda'),
        ('Banani', 'Banani'),
        ('Banasree', 'Banasree'),
        ('Baridhara', 'Baridhara'),
        ('Bashundhara', 'Bashundhara'),
        ('Bawnia', 'Bawnia'),
        ('Beraid', 'Beraid'),
        ('Cantonment area', 'Cantonment area'),
        ('Dakshinkhan', 'Dakshinkhan'),
        ('Dania', 'Dania'),
        ('Demra', 'Demra'),
        ('Dhanmondi', 'Dhanmondi'),
        ('Farmgate', 'Farmgate'),
        ('Gabtali', 'Gabtali'),
        ('Gulshan', 'Gulshan'),
        ('Hazaribagh', 'Hazaribagh'),
        ('Islampur', 'Islampur'),
        ('Jurain', 'Jurain'),
        ('Kafrul', 'Kafrul'),
        ('Kamalapur', 'Kamalapur'),
        ('Kamrangirchar', 'Kamrangirchar'),
        ('Kazipara', 'Kazipara'),
        ('Khilgaon', 'Khilgaon'),
        ('Khilkhet', 'Khilkhet'),
        ('Kotwali', 'Kotwali'),
        ('Lalbagh', 'Lalbagh'),
        ('Matuail', 'Matuail'),
        ('Mirpur', 'Mirpur'),
        ('Mohakhali', 'Mohakhali'),
        ('Mohammadpur', 'Mohammadpur'),
        ('Motijheel', 'Motijheel'),
        ('Nimtoli', 'Nimtoli'),
        ('Pallabi', 'Pallabi'),
        ('Paltan', 'Paltan'),
        ('Ramna', 'Ramna'),
        ('Rampura', 'Rampura'),
        ('Sabujbagh', 'Sabujbagh'),
        ('Sadarghat', 'Sadarghat'),
        ('Satarkul', 'Satarkul'),
        ('Shahbagh', 'Shahbagh'),
        ('Sher-e-Bangla Nagar', 'Sher-e-Bangla Nagar'),
        ('Shyampur', 'Shyampur'),
        ('Sutrapur', 'Sutrapur'),
        ('Tejgaon', 'Tejgaon'),
        ('Uttara', 'Uttara'),
        ('Uttarkhan', 'Uttarkhan'),
        ('Vatara', 'Vatara'),
        ('Wari', 'Wari'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='order', on_delete=models.SET_NULL, null=True
    )
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(verbose_name='Phone Number', max_length=11)
    email = models.EmailField(verbose_name='Email Address', max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=50, choices=AREA)
    order_note = models.CharField(max_length=100, blank=True)
    date = models.DateField(
        verbose_name='Delivery Date',
        auto_now=False,
        auto_now_add=False,
    )
    time = models.TimeField(
        verbose_name='Delivery Time',
        auto_now=False,
        auto_now_add=False,
    )
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.order_number


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
