# coding=UTF-8
from dal import autocomplete
from django import forms

from news.models import MacSkill


class MacSkillForm(forms.ModelForm):

    class Meta:
        model = MacSkill
        fields = '__all__'
        widgets = {
            'volume': autocomplete.ModelSelect2(
                url='news:volume-autocomplete',
                attrs={
                    'data-placeholder': u'输入节目期号或者标题...',
                    'data-minimum-input-length': 2,
                })
        }
