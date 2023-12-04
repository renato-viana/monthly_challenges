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
    "december": "Give a compliment to someone every day!"
}


# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported!")
