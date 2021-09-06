from django.shortcuts import render


def index(request):
    context = {
        'svelte_js': 'build/hello_world/index.js', 
        'svelte_css': 'build/hello_world/index.css', 
        'title': 'Django Svelte Template | Home'
    }
    return render(request, 'svelte_template.html', context=context)


def another_page(request):
    context = {
        'svelte_js': 'build/hello_world/another_page.js', 
        'svelte_css': 'build/hello_world/another_page.css', 
        'title': 'Django Svelte Template | Another Page'
    }
    return render(request, 'svelte_template.html', context=context)
