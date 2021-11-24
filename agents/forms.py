from django import forms
from leads.models import Agent
from leads.models import User


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )


class PhotoAddUpdateAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'agent_photo',
        )

