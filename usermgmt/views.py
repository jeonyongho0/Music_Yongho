from django.shortcuts import render
from .filters import MemberFilter

def search(request):
    user_list = Member.objects.all()
    members = MemberFilter(request.GET, queryset=user_list)
    return render(request, 'usermgmt/list_search.html', {'filter': members})
