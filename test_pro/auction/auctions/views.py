from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, Bidder
from auctions.serializers import BidderSerializer, VendorSerializer


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


@api_view(['POST'])
def register(request):
    """
    Registeration form
    """
    try:
        if request.method == "POST":
            type = request.data.pop('type')
            if type == "Vendor":
                serializer = VendorSerializer(data=request.data)
            elif type == "Bidder":
                serializer = BidderSerializer(data=request.data)
            else:
                raise Exception
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return str(e)


@api_view(['POST'])
def login(request):
    """
    Login
    """
    try:
        if request.method == "POST":
            type = request.data.pop('type')
            email = request.data.pop('email')
            password = request.data.pop('password')
            if type == "Vendor":
                vendors = Vendor.objects.all()
                vendor = vendors.get(email=email, password=password)
                serializer = VendorSerializer(vendor)
            elif type == "Bidder":
                bidders = Bidder.objects.all()
                bidder = bidders.get(email=email, password=password)
                serializer = BidderSerializer(bidder)
            else:
                raise Exception
            if serializer.data:
                return Response(f"Hi {serializer.data.get('first_name')}! You are a great {type}", status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return str(e)
