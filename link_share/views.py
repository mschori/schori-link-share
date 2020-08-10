from django.shortcuts import render


def cs50_links(request):
    return render(request, 'link_share/cs50_links.html')
