from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json


@ensure_csrf_cookie
def index(request):
    context = {
        'svelte_js': 'build/hello_world/index.js', 
        'svelte_css': 'build/hello_world/index.css', 
        'title': 'Django Svelte Template | Home'
    }
    return render(request, 'svelte_template.html', context=context)


@ensure_csrf_cookie
def another_page(request):
    context = {
        'svelte_js': 'build/hello_world/another_page.js', 
        'svelte_css': 'build/hello_world/another_page.css', 
        'title': 'Django Svelte Template | Another Page'
    }
    return render(request, 'svelte_template.html', context=context)


def json_endpoint(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        print(post_data)
        return JsonResponse({'status': 'received data correctly!'})
    else:
        return JsonResponse({'error': 'only post requests allowed'})
