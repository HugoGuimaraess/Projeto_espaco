from django.contrib import admin
from apps.galeria.models import Fotografia
# Register your models here.



class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id','nome','categoria','usuario','publicada','legenda')
    list_display_links = ('id','nome')
    list_per_page = (10)
    list_filter = ('categoria','usuario')
    list_editable = ('publicada',)
    search_fields = ('nome',)










admin.site.register(Fotografia,ListandoFotografia)
