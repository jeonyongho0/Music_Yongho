from django import forms
import django_filters
from usermgmt.models import Member


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = {
            'music_price' : ['price']
        }
