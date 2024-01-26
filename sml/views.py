from django.shortcuts import render
from .forms import URL_postform
from .models import URLdata
import string, random

def generator(all_codes):
    characters = string.ascii_letters + string.digits + string.punctuation
    while(True):
        encoded = ''.join(random.choice(characters) for i in range(15))
        if encoded not in all_codes:
            return encoded
        encoded = ""

# Create your views here.
def Home(request):
    if request.method == 'POST':
        actual_url = request.POST.get('long_url')
        name_link = request.POST.get('name')
        stored_tag = URLdata.objects.create(
            name = name_link,
            long_url = actual_url,
        )
        all_codes = URLdata.objects.all().values_list('short_code', flat=True)
        encoded = generator(all_codes)
        stored_tag.short_code = encoded
        stored_tag.save()
    url_form = URL_postform()
    variables = {
        'url_form': url_form,
    }
    return render(request, 'sml/home.html', variables)

def ViewAll(request):
    all_codes = URLdata.objects.all()
    for code in all_codes:
        link_to = f"{code.long_url}"
        shorty = code.short_code
        if "href" not in shorty:
            code.short_code = code.short_code.replace(f"{shorty}", f'<a href="{link_to}" target="_blank">{shorty}</a>')
    variables = {
        'all_codes': all_codes,
    }
    return render(request, 'sml/view_codes.html', variables)