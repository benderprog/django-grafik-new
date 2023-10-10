from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Person, Rank


def peoples_list(request: HttpRequest) -> HttpResponse:
    peoples = (
        Person
        .objects
        .order_by("pk")
        .prefetch_related("rank")
        .all()
    )
    return render(
        request=request,
        template_name="peoples/index.html",
        context={"peoples": peoples},
    )


