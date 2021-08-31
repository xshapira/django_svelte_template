from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'svelte_js': 'build/hello_world/index.js', 'svelte_css': 'build/hello_world/index.css'})


def another_page(request):
    return render(request, 'index.html', {'svelte_js': 'build/hello_world/another_page.js', 'svelte_css': 'build/hello_world/another_page.css'})
