from django.shortcuts import render
import random
import string


def randomm(request):
    list_string = string.ascii_uppercase + string.ascii_lowercase
    list_digits = "0123456789"
    list_specials = "!№;%:?*()_+"
    digits = request.GET.getlist('digits')
    specials = request.GET.getlist('specials')
    length = request.GET.get('length')
    if length == None:
        length = 0
    if not 1 <= int(length) <= 100:
        return render(request, 'randomm/warning_random.html', context={'length':length})
    else:
        if digits:
            list_string += list_digits
        if specials:
            list_string += list_specials
        output_randoms = str()
        for _ in range(int(length)):
            output_randoms += random.choice(list_string)
        return render(request, 'randomm/random.html', context={'output_randoms':output_randoms})
