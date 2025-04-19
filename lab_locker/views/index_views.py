from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

async def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

