import datetime
import random

from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        "name": "Mohira",
        "age": random.randint(1, 25),
        "time": datetime.datetime.now().strftime('%Y.%m.%d'),
        "a": random.randint(1, 1000),
        "b": random.randint(-100, 1000),
    }
    c = context['a'] + context['b']
    c1 = context['a'] * context['b']
    return HttpResponse(f"""<h1 style: 'color: blue;'>{context["name"]} ning yoshi {context["age"]} da.</h1>"""
                        f"""<p>Bugungi sana: <code>{context["time"]}</code></p>
                        <p>{context['a']} + {context['b']} = {c}</p>
                        <p>{context['a']} * {context['b']} = {c1}</p>""")
