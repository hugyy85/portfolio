from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.template.context_processors import csrf
from .query import how_long_month, parse_dict, parse_phones
import gc, json


def show_details(request, number):
    # показывает развернутую информацию о звонках по выбранному номеру

    data_storage = json.loads(request.session['details'])
    result = parse_dict(data_storage, str(number))

    return render(request, 'details.html', context={'lines': result})


def upload_file(request):

    args = {'form': UploadFileForm()}
    args.update(csrf(request))

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file')
            numbers = parse_phones(files)
            if not numbers:
                return redirect('/phone_calls/error/')
            data_storage = how_long_month(numbers)
            request.session['details'] = json.dumps(data_storage)

            return redirect('/phone_calls/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', args)


def start(request):
    # Garbage Collector
    gc.collect()

    args = {'form': UploadFileForm}
    args.update(csrf(request))

    return render(request, 'upload.html', args)


def success(request):
    data_storage = json.loads(request.session['details'])
    return render(request, request, 'success.html', context={'dict': data_storage})


def error(requset):
    return render(request, 'error.html')

