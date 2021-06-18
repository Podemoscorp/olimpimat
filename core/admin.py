from django.contrib import admin
from .models import Image, Olimpimat, Challenge, Contribute, Sponsor, New

# Register your models here.
class AdminImages(admin.ModelAdmin):
    list_display = ("id", "name", "upload_in")
    list_display_links = ("id", "name", "upload_in")
    search_fields = ("id", "name", "upload_in", "image")
    list_per_page = 20


class AdminOlimpiada(admin.ModelAdmin):
    list_display = ("id", "nome", "criado_em")
    list_display_links = ("id", "nome", "criado_em")
    search_fields = ("id", "nome", "criado_em", "descricao")
    list_per_page = 20


class AdminChallenge(admin.ModelAdmin):
    list_display = ("id", "data_de_inicio", "data_de_termino", "criado_em")
    list_display_links = ("id", "data_de_inicio", "data_de_termino", "criado_em")
    search_fields = (
        "id",
        "descricao",
        "data_de_inicio",
        "data_de_termino",
        "criado_em",
    )
    list_per_page = 20


class AdminNews(admin.ModelAdmin):
    list_display = ("id", "title", "poster", "abstract", "posted_in")
    list_display_links = ("id", "title", "poster", "abstract", "posted_in")
    search_fields = ("id", "title", "poster", "abstract", "posted_in", "content")
    list_per_page = 20


admin.site.register(Image, AdminImages)
admin.site.register(Olimpimat, AdminOlimpiada)
admin.site.register(Challenge, AdminChallenge)
admin.site.register(Contribute)
admin.site.register(Sponsor)
admin.site.register(New, AdminNews)
