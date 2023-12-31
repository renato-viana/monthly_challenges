from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a book every week!",
    "may": "Go to the gym every day!",
    "june": "Eat 5 portions of fruits or vegetables every day!",
    "july": "Drink 8 glasses of water daily!",
    "august": "Learn a new language for 15 minutes every day!",
    "september": "Write in a journal every day!",
    "october": "Spend 30 minutes outdoors every day!",
    "november": "Practice mindfulness for 10 minutes daily!",
    "december": None
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
