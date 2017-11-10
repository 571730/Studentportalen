from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Emne, Studie, Vurdering
from .forms import VurderingForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    emne_vansk = Emne.objects.order_by('-vanskelig')[:3]
    emne_arb = Emne.objects.order_by('-arbeid')[:3]
    emne_inte = Emne.objects.order_by('-interesse')[:3]
    emne_anta = Emne.objects.order_by('-antall')[:3]

    context = {'emn_vansk': emne_vansk, 'emne_arb': emne_arb, 'emne_inte': emne_inte, 'emne_anta': emne_anta}

    return render(request, 'Studentportalen/index_django.html', context)


def finnPoeng(emne):

    vurderinger = Vurdering.objects.filter(emne__exact=emne)

    teller, vansk, arb, inte = 0, 0, 0, 0

    for vurd in vurderinger:
        teller += 1
        vansk += vurd.vanskelig
        arb += vurd.arbeid
        inte += vurd.interesse

    if teller != 0:
        vansk, inte, arb = (vansk / teller), (inte / teller), (arb / teller)

    return vansk, inte, arb


def emner(request):
    emner = Emne.objects.all()

    return render(request, 'Studentportalen/emner_django.html', {'emner': emner})


def fag(request, emne_id):

    emne = get_object_or_404(Emne, pk=emne_id)
    vurderinger = Vurdering.objects.filter(emne__exact=emne)

    teller, vansk, arb, inte = 0, 0, 0, 0

    for vurd in vurderinger:
        teller += 1
        vansk += vurd.vanskelig
        arb += vurd.arbeid
        inte += vurd.interesse

    if teller != 0:
        vansk, inte, arb = (vansk/teller), (inte/teller), (arb/teller)

    width_vansk = int((100 / 5) * vansk)
    width_int = int((100 / 5) * inte)
    width_arb = int((100 / 5) * arb)
    vansk, inte, arb = round(vansk, 1), round(inte, 1), round(arb, 1)
    width = {'vansk': width_vansk, 'int': width_int, 'arb': width_arb}
    verdi = {'vansk': vansk, 'inte': inte, 'arb': arb}

    if request.method == 'POST':

        form = VurderingForm(request.POST or None)
        if form.is_valid():
            vurdering = form.save(commit=False)
            vurdering.bruker = request.user
            vurdering.emne = emne
            vurdering.save()
            vurderinger_2 = Vurdering.objects.filter(emne__exact=emne)
            emne_kalk(emne_id)
            return redirect(request.path_info)

    else:
        form = VurderingForm()

        return render(request, 'Studentportalen/fag_django.html', {'emne': emne, 'width': width, 'form': form,
                                                                   'verdi': verdi, 'vurderinger': vurderinger})


def emne_kalk(emne_id):
    emne = get_object_or_404(Emne, pk=emne_id)
    vurderinger = Vurdering.objects.filter(emne__exact=emne)

    teller, vansk, arb, inte = 0, 0, 0, 0

    for vurd in vurderinger:
        teller += 1
        vansk += vurd.vanskelig
        arb += vurd.arbeid
        inte += vurd.interesse

    if teller != 0:
        vansk, inte, arb = (vansk / teller), (inte / teller), (arb / teller)

    emne_antall = teller

    emne.vanskelig = round(vansk, 1)
    emne.interesse = round(inte, 1)
    emne.arbeid = round(arb, 1)
    emne.antall = emne_antall
    emne.save()


def login_view(request):
    form = LoginForm

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

        else:

            return render(request, 'Studentportalen/logg_inn.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'Studentportalen/logg_inn.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:

                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("/")

            else:
                return render(request, 'Studentportalen/registrering.html',
                              {'form': form, 'error_message': 'Passordene er ikke like'})
        else:
            return render(request, 'Studentportalen/registrering.html',
                          {'form': form, 'error_message': 'Brukernavnet er tatt'})

    else:
        form = UserForm()
        context = {
            "form": form,
        }
        return render(request, 'Studentportalen/registrering.html', context)
