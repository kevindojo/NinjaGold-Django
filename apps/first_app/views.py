from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def goldrandom(lower, upper):                   #algo to produce random values
    import random
    goldrand = random.randrange(lower,upper)

    return goldrand



def index(request):
    return render(request, 'ninjagold/index.html')

def process(request,location):
    goldearn = {
                'farm': goldrandom (10,21),
                'cave': goldrandom (5,11),
                'house': goldrandom (2,6),
                'casino': goldrandom (-50,51)
                }

    request.session['gold'] = goldearn[location]    # locatoin associated with 'name' in html
    
    
    gold = request.session['gold']           # defined for gold earned from each location
    time = datetime.now().strftime(" -add on %H:%M %p, %B, %d, %Y")

    # print goldearn[location]
    # print location

    try:
        request.session ['total']       
    except KeyError:
        request.session['total'] = 0    #running total, "your gold"
    request.session['total'] += gold    #gold total
    print request.session['total']

            ##### to make the log continuous#####

    if 'activities' not in request.session:     # making activities log
        request.session['activities'] = []      
    else:
        request.session['activities'] = request.session['activities']

    if gold < 0:
        activity = "Entered a {} and loss {}! OUCH {}".format(location, gold, time)
    else:
        activity = "Earned {} gold(s) from the {}! {}".format(gold, location, time)

    
    log = {
            'activity': activity
            }

    request.session['activities'].append(log)
    print request.session['activities']

    return redirect ('/')






def clear(request):
    del request.session['total']
    del request.session['activities']
    return redirect ('/')