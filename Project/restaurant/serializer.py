from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source='reservation_date')
    time = serializers.IntegerField(source='reservation_slot')
    guests = serializers.CharField(source='first_name')

    class Meta:
        model = Booking
        fields = ["date", "time", "guests", "occasion"]