from django.contrib import admin
from .models import hostDetails, visitor, isVisited

admin.site.register(hostDetails)
admin.site.register(visitor)
admin.site.register(isVisited)
