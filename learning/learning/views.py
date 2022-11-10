from django.http import HttpResponse  # import HttpResponse for text response

def aboutUS(request):
    return HttpResponse('<center><h1>Welcome to the about us page</h1></center>')

def contactUS(request):
    return HttpResponse('<center><h1>Welcome to the contact us page</h1></center>')


# View for dynamic url
def dynamic(request, my_name):
    # print(type(my_name))
    return HttpResponse(f'<center><h1>Hello \"{my_name}\"</h1></center>')

def dynamic_slug(request, my_slug):
    # print(type(my_slug))
    return HttpResponse(f'<center><h1>Hello \"{my_slug}\"</h1></center>')

def dynamic_int(request, my_int):
    # print(type(my_int))
    return HttpResponse(f'<center><h1>Hello \"{my_int}\"</h1></center>')

def dynamic_auto(request, auto):
    # print(type(my_auto))
    return HttpResponse(f'<center><h1>Hello \"{auto}\"</h1></center>')