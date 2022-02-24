from django.urls import path
from challenges import views

# URLConf
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month_id>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="str_monthly_challenge"),
]
