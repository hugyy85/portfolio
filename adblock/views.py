from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from .forms import SiteForm
from adblock.read_html import FindText
from django.contrib import sessions


def index(request):
    args = {'form': SiteForm()}
    args.update(csrf(request))
    if request.session.get('text'):
        args.setdefault('text', request.session['text'])
    return render(request, 'adblock/adblock_index.html', args)


def block(request):

    if request.method == 'POST':
        form = SiteForm(request.POST)

        if form.is_valid():
            site = request.POST['site']
            list_tags = FindText(site).find_text()

            request.session['text'] = list_tags
        else:
            text = 'Не найдено'

    return redirect('/adblock/')