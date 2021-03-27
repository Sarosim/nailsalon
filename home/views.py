from django.shortcuts import render


# Create your views here.
def index(request):
    """ Render the home page"""

    # Special banner settings
    banner_context = {
        'banner_display': False,
        'banner_pos_left': '60vw',
        'banner_pos_top': '15vh',
        'banner_width': '25vw',
        'banner_text_1': 'Want to ',
        'banner_button': 'get',
        'banner_text_2': 'a FREE treatment?',
    }
    return render(request, "home/index.html", banner_context)