from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request, 
        "newyear/index.html", 
        {
            "itsnewyear": datetime.now().month == 1 and datetime.now().day == 1
        }
    )