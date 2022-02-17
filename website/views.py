from django.shortcuts import render

# Create your views here.


def index_view(request):
    content={"name":"Majid","lastname":"Karimi"}
    return render(request, "index.html", content)