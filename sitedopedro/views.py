from django.shortcuts import render, redirect
from .models import SitesDeReceitas, MelhoresReceitas


# Create your views here.
def home (request):
  sites = SitesDeReceitas.objects.all()
  comidas = MelhoresReceitas.objects.all()
  print(sites)
  print(comidas)
  return render (request, "home.html", context={'sites': sites,'comidas':comidas})

def create_comida(request):
  if request.method == 'POST':
    print(request.POST)
    MelhoresReceitas.objects.create(
      nome = request.POST['nome'],
      origem = request.POST['origem'],
      nota = request.POST['nota'],
      tipo = request.POST['tipo'],
    )
    return redirect('home')
  return render(request, 'forms.html')

def update_comida(request,id):
  comida = MelhoresReceitas.objects.get(id = id)
  if request.method == 'POST':
    comida.nome = request.POST['nome'],
    comida.origem = request.POST['origem'],
    comida.nota = request.POST['nota'],
    comida.tipo = request.POST['tipo'],
    comida.save()

    return redirect('home')
  return render(request, 'forms.html', context={"action": "Atualizar","comida": comida})

def delete_comida(request, id):
  comida = MelhoresReceitas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      comida.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"comida": comida})