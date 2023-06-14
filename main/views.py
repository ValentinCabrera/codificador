from django.shortcuts import render
from django.http import HttpResponse
from logic.main import code
from logic.graphic import remove_graphic

def main_view(request):
    if request.method == 'POST':
        try:
            previous_file = request.session['file_name']
            remove_graphic(previous_file)

        except:
            pass

        binario = request.POST.get("entrada")
        metodo = request.POST.get("metodo")
        file_name = code(binario, metodo)
        return render(request, 'main.html', {'file_name': file_name})

    return render(request, 'main.html')
