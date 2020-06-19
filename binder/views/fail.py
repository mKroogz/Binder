from django.shortcuts import render

def fail(request):
    if request.method == 'GET':
        template = 'fail.html'
        context = {}

        return render(request, template, context)