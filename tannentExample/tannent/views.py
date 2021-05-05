from django.shortcuts import render
from .models import Member
from .utilities import get_tenant


def our_teams(request):
    tanant = get_tenant(request)
    members = Member.objects.filter(tanant=tanant)
    return render(request, 'tanant/our_team.html', {'tenant':tanant, 'members': members})

