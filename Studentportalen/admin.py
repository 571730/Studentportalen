from django.contrib import admin

from .models import Emne, Studie, Vurdering

admin.site.register(Emne)
admin.site.register(Studie)
admin.site.register(Vurdering)
