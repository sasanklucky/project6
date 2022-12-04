from django.shortcuts import render

# Create your views here.
def lucky(request):
    d={"a":5,"b":2}
    return render(request,'lucky.html',d)