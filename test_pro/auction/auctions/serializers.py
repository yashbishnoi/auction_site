from rest_framework import serializers
from .models import Vendor, Bidder


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'company_name', 'mobile', 'telephone', 'address_line1', 'address_line2',
                  'city', 'pincode', 'country', 'state',
                  )


class BidderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bidder
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'company_name', 'mobile', 'telephone', 'address_line1', 'address_line2',
                  'city', 'pincode', 'country', 'state',
                  )
