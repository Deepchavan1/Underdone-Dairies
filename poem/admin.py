from django.contrib import admin
from poem.models import Poem, PoemComment

admin.site.register((Poem))
admin.site.register((PoemComment))
# @admin.register(Poem)