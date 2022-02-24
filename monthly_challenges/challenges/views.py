from ast import arg
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    "january": "jan",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december",
}


def index(req):
    month_list_items = ""

    for month in challenges:
        month_url = reverse("str_monthly_challenge", args=[month])
        month_list_items += f'<li><a href="{month_url}">{month}</a></li>'

    month_list = f"<ul>{month_list_items}</ul>"

    return HttpResponse(month_list)


def monthly_challenge(req, month):
    try:
        month_data = challenges[month]
        return render(
            req, "challenges/challenge.html", {"month": month, "text": month_data}
        )
    except:
        return HttpResponseNotFound(month + " Not Found")


def monthly_challenge_by_number(req, month_id):
    try:
        month = list(challenges.keys())[month_id - 1]
        redirect_url = reverse("str_monthly_challenge", args=[month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("month id: " + str(month_id) + " Not Found")
