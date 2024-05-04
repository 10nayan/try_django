from django.http import HttpResponse

HTMLSTRING = """
<h1>Hello World</h1>
"""

def home_view(request):
    return HttpResponse(HTMLSTRING)