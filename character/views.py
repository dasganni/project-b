from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from guardian.admin import GuardedModelAdmin

# Create your views here.
@login_required
def editCharacters(request):
    return render(request, 'characters/editCharacters.html', {})
