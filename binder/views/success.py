from django.shortcuts import render

def success(request):
    if request.method == 'GET':
        template = 'success.html'
        context = {}

        return render(request, template, context)