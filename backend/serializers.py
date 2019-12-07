from rest_framework import serializers
from .models import Client, User, Location, Test_Standard, Product, Certificate, Test_Sequence, Performance_Data, \
    Service


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name', 'client_type', 'client_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'fname', 'lname', 'mname', 'job_title', 'email', 'ophone', 'cphone', 'prefix', 'client_ID')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address1', 'address2', 'city', 'state', 'postal_code', 'phone_number', 'fax_number', 'client_ID')


class TestStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test_Standard
        fields = ('standard_name', 'description', 'published_date')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'product_name', 'cell_technology', 'cell_manufacturer', 'number_of_cells', 'number_of_cells_in_series',
            'number_of_series_strings', 'number_of_diodes', 'product_length', 'product_width', 'product_weight',
            'superstate_type', 'superstate_manufacturer', 'substrate_type', 'substrate_manufacturer', 'frame_type',
            'frame_adhesive', 'encapsulation_type', 'encapsulation_manufacturer', 'junction_box_type',
            'junction_box_manufacturer')


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'certificate_ID', 'user_ID', 'report_number', 'issue_date', 'standard_ID', 'location_ID', 'model_number')


class TestSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test_Sequence
        fields = 'sequence_name'


class PerformanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance_Data
        fields = ('model_number', 'sequence_ID', 'max_system_volage', 'voc', 'lsc', 'vmp', 'imp', 'pmp', 'ff')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_name', 'description', 'is_FI_required', 'FI_frequency', 'standard_ID')
