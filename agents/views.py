from django.urls import reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin


class AgentListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('agents:agents_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agents_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)