from django.db import models

# Create your models here.


class CountryName:
    AMERICA = 1
    GERMANY = 2
    AUSTRALIA = 3
    FRANCE = 4


class Vendor(models.Model):
    COUNTRY_CHOICES = (
        (CountryName.AMERICA, 'America'),
        (CountryName.GERMANY, 'Germany'),
        (CountryName.AUSTRALIA, 'Australia'),
        (CountryName.FRANCE, 'France'),
    )

    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    telephone = models.CharField(max_length=64, blank=True, null=True)
    address_line1 = models.CharField(max_length=100, blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    country = models.IntegerField(
        blank=True, null=True, choices=COUNTRY_CHOICES,
    )
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name_plural = 'Vendors'


class Bidder(models.Model):
    COUNTRY_CHOICES = (
        (CountryName.AMERICA, 'America'),
        (CountryName.GERMANY, 'Germany'),
        (CountryName.AUSTRALIA, 'Australia'),
        (CountryName.FRANCE, 'France'),
    )

    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    telephone = models.CharField(max_length=64, blank=True, null=True)
    address_line1 = models.CharField(max_length=100, blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    country = models.IntegerField(
        blank=True, null=True, choices=COUNTRY_CHOICES,
    )
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name_plural = 'Bidders'
