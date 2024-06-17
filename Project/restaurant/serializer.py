from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source='reservation_date')
    time = serializers.IntegerField(source='reservation_slot')
    guests = serializers.CharField(source='first_name')

    class Meta:
        model = Booking
        fields = ["date", "time", "guests", "occasion"]

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   class Meta:
        model = Menu
        fields = ["name", "price", "description"]
