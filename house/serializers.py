from rest_framework import serializers
from django.conf import settings
from .models import Infra, Hobby, Lifestyle, Region ,Center, CenterReview, Cart, Report

class InfraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infra
        fields = ['id', 'name']

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'name']

class LifestyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifestyle
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):

    lifename = serializers.SerializerMethodField()
    hobbyname = serializers.SerializerMethodField()
    infraname = serializers.SerializerMethodField()

    class Meta:
        model=Region
        fields = [
            'id', 'lstyle_id', 'infra_id', 'hobby_id', 'city_code', 'city', 'gugoon',
            'longtitude', 'latitude', 'thumbnail', 'lifename', 'hobbyname', 'infraname'
        ]
        #fields=[ 'id', 'lstyle_id', 'infra_id', 'hobby_id', 'city_code','city', 'gugoon', 'longtitude', 'latitude', 'thumbnail']
    def get_lifename(self, obj):
        return [lifestyle.name for lifestyle in obj.lstyle_id.all()]

    def get_hobbyname(self, obj):
        return [hobby.name for hobby in obj.hobby_id.all()]

    def get_infraname(self, obj):
        return [infra.name for infra in obj.infra_id.all()]



class CenterSerializer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField()
    gugoon = serializers.SerializerMethodField()

    class Meta:
        model = Center
        fields = ['id', 'name', 'region_id', 'address', 'time', 'cost', 'longtitude', 'latitude', 'thumbnail', 'city','gugoon']

    def city(self, obj):
        return obj.city()
    def gugoon(self, obj):
        return obj.gugoon()

    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())
    # class Meta:
    #     model=Center
    #     fields="__all__"


class CartSerializer(serializers.ModelSerializer):
    center1 = CenterSerializer()
    center2 = CenterSerializer()
    center3 = CenterSerializer()
    center4 = CenterSerializer()
    center5 = CenterSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'center1', 'center2', 'center3', 'center4', 'center5', 'total_cost']

class CartcostSerializer(serializers.ModelSerializer):
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2) #소숫점 포함 10자리
    class Meta:
        model=Cart
        fields= ['total_cost']

class FilterSerializer(serializers.Serializer):
    # 각 필드를 정수 리스트로 선언
    infra = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )
    hobby = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )
    lifestyle = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )

class CenterReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CenterReview
        fields = ['center_id', 'user_id', 'content']

class ReportSerializer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField()
    gugoon = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['user_id', 'region_id', 'plan1', 'plan2', 'plan3', 'city', 'gugoon']

    def city(self, obj):
        return obj.city()
    def gugoon(self, obj):
        return obj.gugoon()

    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())