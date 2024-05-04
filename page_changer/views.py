from django.shortcuts import render

# Create your views here.
def to_test_page(req):
    return render(req, "test.html")