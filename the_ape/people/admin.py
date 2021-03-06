from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from people.models import Person, HouseTeam


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'videos': FilteredSelectMultiple(verbose_name='videos', is_stacked=False),
        }


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['name', 'teaches', 'performs', 'house_team', 'headshot', 'active']
    list_filter = ['teaches', 'performs']
    form = PersonForm

    def get_queryset(self, request):
        return Person.all_objects


class HouseTeamForm(forms.ModelForm):

    class Meta:
        model = HouseTeam
        fields = '__all__'
        widgets = {
            'videos': FilteredSelectMultiple(verbose_name='videos', is_stacked=False),
        }


class PerformerInline(admin.TabularInline):
    model = Person
    readonly_fields = ['name']
    fields = ['name']
    extra = 0


class HouseTeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = PersonForm
    inlines = [
        PerformerInline,
    ]


admin.site.register(Person, PersonAdmin)
admin.site.register(HouseTeam, HouseTeamAdmin)
