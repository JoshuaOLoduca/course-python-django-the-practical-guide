from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

challenges = {
  'january': 'jan',
  'february': 'february',
  'march': 'march',
  'april': 'april',
  'may': 'may',
  'june': 'june',
  'july': 'july',
  'august': 'august',
  'september': 'september',
  'october': 'october',
  'november': 'november',
  'december': 'december',
}

def monthly_challenge(req, month):
  try:
    return HttpResponse(challenges[month])
  except:
    return HttpResponseNotFound(month + ' Not Found')
    

def monthly_challenge_by_number(req, month_id):
  try:
    month = list(challenges.keys())[month_id - 1]
    return HttpResponseRedirect('/challenges/' + month)
  except:
    return HttpResponseNotFound('month id: ' + str(month_id) + ' Not Found')
