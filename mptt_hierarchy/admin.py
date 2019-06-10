from django.contrib import admin
from mptt_hierarchy.models import File
from mptt.admin import DraggableMPTTAdmin

admin.site.register(File, DraggableMPTTAdmin)
