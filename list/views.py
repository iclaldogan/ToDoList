from django.shortcuts import render, get_object_or_404, redirect
from .models import Gorev
from .forms import GorevForm

def gorev_list(request):
    gorevler = Gorev.objects.all().order_by('-olusturulma_tarihi')
    return render(request, 'list/gorev_list.html', {'gorevler': gorevler})

def gorev_ekle(request):
    if request.method == 'POST':
        form = GorevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gorev_list')
    else:
        form = GorevForm()
    return render(request, 'list/gorev_form.html', {'form': form})

def gorev_guncelle(request, pk):
    gorev = get_object_or_404(Gorev, pk=pk)
    if request.method == 'POST':
        form = GorevForm(request.POST, instance=gorev)
        if form.is_valid():
            form.save()
            return redirect('gorev_list')
    else:
        form = GorevForm(instance=gorev)
    return render(request, 'list/gorev_form.html', {'form': form})

def gorev_sil(request, pk):
    gorev = get_object_or_404(Gorev, pk=pk)
    if request.method == 'POST':
        gorev.delete()
        return redirect('gorev_list')
    return render(request, 'list/gorev_sil.html', {'gorev': gorev})
