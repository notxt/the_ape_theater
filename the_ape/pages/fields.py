import re

from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.utils.functional import curry

color_re = re.compile('^#([A-Fa-f0-9]{6})$')
validate_color = RegexValidator(color_re, 'Enter a valid color.', 'invalid')


class SortedManyToManyField(models.ManyToManyField):

    def __init__(self, *args, **kwargs):
        self.sort_column = kwargs.pop('sort_column', 'sort_order')
        super(SortedManyToManyField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['form_class'] = SortedModelMultipleChoiceField
        result = super(SortedManyToManyField, self).formfield(**kwargs)
        return result

    def value_from_object(self, obj):
        # use the through relation's sort column as the data ordering when generating a form field
        related_target_name = self.m2m_reverse_target_related_name()
        ordering = '__'.join([related_target_name, self.sort_column])

        qs = super(SortedManyToManyField, self).value_from_object(obj)
        return qs.order_by(ordering)

    def contribute_to_related_class(self, cls, related):
        super(SortedManyToManyField, self).contribute_to_related_class(cls, related)
        get_m2m_reverse_rel = curry(self._get_m2m_reverse_attr, related, 'rel')
        self.m2m_reverse_target_related_name = lambda: get_m2m_reverse_rel().related_name

    def save_form_data(self, instance, data):
        if instance.pk:
            field = getattr(instance, self.attname)
            field.clear()
            for i, related in enumerate(data):
                kwargs = {
                    self.m2m_field_name(): instance,
                    self.m2m_reverse_field_name(): related,
                    self.sort_column: i
                }
                self.rel.through.objects.create(**kwargs)
        return instance


class SortedModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def clean(self, value):
        if len(value) > len(set(value)):
            raise ValidationError("Cannot have duplicates")

        qs = super(SortedModelMultipleChoiceField, self).clean(value)  # get all results in one query
        by_pk = dict([(str(b.pk), b) for b in qs])  # make them easily fetchable by primary key
        sorted_models = [by_pk[pk] for pk in value]
        return sorted_models


class ColorWidget(forms.TextInput):

    def extra_css_classes(self):
        return ['color']

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        extra_class = ' '.join(self.extra_css_classes())
        if 'class' in attrs:  # already defined, so append our color class
            attrs['class'] += ' ' + extra_class
        else:
            attrs['class'] = extra_class
        super(ColorWidget, self).__init__(*args, **kwargs)


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)
