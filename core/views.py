from django.shortcuts import render, redirect, get_object_or_404
from core.models import Olimpimat, Challenge, Contribute, Sponsor, New
from django.core.paginator import Paginator
from django.contrib import auth, messages

# Create your views here.
def index(request):
    olimpiada = Olimpimat.objects.all().order_by("id").last()
    challenges = (
        Challenge.objects.all().filter(edicao_olimpiada=olimpiada).order_by("-id")
    )

    paginator = Paginator(challenges, 15)
    page_number = 1
    if "page" in request.GET:
        page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    len_challenges = challenges.count()

    return render(
        request,
        "pages/index.html",
        {
            "challenges": page_obj,
            "olimpiada": olimpiada,
            "len_challenges": len_challenges,
        },
    )


def olimpimat(request, id):
    olimpiada = get_object_or_404(Olimpimat, pk=id)
    challenges = (
        Challenge.objects.all().filter(edicao_olimpiada=olimpiada).order_by("id")
    )
    return render(
        request,
        "pages/olimpimat.html",
        {"challenges": challenges, "olimpiada": olimpiada},
    )


def challenge(request, id):
    challenge = get_object_or_404(Challenge, pk=id)

    return render(request, "pages/challenge.html", {"challenge": challenge})


def edicoes_passadas(request):
    olimpiadas = Olimpimat.objects.all().order_by("id")[1:]
    return render(request, "pages/passadas.html", {"olimpiadas": olimpiadas})


def realizacao(request):
    contributes = Contribute.objects.all().order_by("id")
    return render(request, "pages/realicacao.html", {"contributes": contributes})


def patrocinadores(request):
    patrocinadores = Sponsor.objects.all()
    return render(
        request, "pages/patrocinadores.html", {"patrocinadores": patrocinadores}
    )


def noticias(request):
    if request.is_ajax():
        ...
    else:
        ultimas = New.objects.all().order_by("-posted_in")[:6]

        noticias = New.objects.all().order_by("id")

        if "order" in request.GET:
            ...
        else:
            noticias.order_by("-posted_in")

        paginator = Paginator(noticias, 30)
        page_number = 1
        if "page" in request.GET:
            page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        dados = {
            "ultimas": ultimas,
            "noticias": page_obj,
        }

        return render(request, "pages/noticias.html", dados)


def noticia(request, id):
    if not New.objects.filter(id=id).exists():
        messages.success(request, "Postagem não encontrada.")
        return redirect("index")

    new = New.objects.filter(id=id).get()

    if new.visibility == "A":
        if request.user.is_anonymous:
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("login")
        if new.poster_id != request.user.id:
            messages.success(
                request, "Você não tem autorização para acessar esta postagem."
            )
            return redirect("index")

    new.views = new.views + 1
    new.save()

    return render(request, "pages/noticia.html", {"new": new})
