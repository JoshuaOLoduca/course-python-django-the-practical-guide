from django.shortcuts import render
from django.http import HttpResponse

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

def monthly_challenge(req, month):
  return HttpResponse(challenges[month])

def monthly_challenge_by_number(req, month):
  return HttpResponse("number")