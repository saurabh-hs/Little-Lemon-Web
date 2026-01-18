from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuTable, Booking
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer    
    permission_classes = [IsAuthenticated]