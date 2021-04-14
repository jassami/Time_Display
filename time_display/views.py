from django.shortcuts import render
from time import gmtime, strftime
from pytz import timezone
from datetime import datetime

def index(request):
    dt = datetime.now(timezone("US/Central"))
    context = {
        'date': strftime("%B %d, %Y", gmtime()),
        'time': dt.strftime("%I:%M %p"),
    }
    return render(request, 'index.html', context)
# Create your views here.
