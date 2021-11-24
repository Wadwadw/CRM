import random
from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm, PhotoAddUpdateAgentForm
from .mixins import OrganiserAndLoginRequiredMixin
from django.contrib.auth import get_user_model


User = get_user_model()


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
        string = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        random_password = ''.join((random.choice(string) for i in range(15)))
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{random_password}")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        send_mail(
            subject='You agent now',
            message=f'You have bin invited in to CRM system, your username is "{user.username}",'
                    f' and your password is "{random_password}"',
            from_email='vadym@mail.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leads"] = self.object.leads.all()
        return context

    def get_queryset(self):
        organization = self.request.user.userprofile
        agent = Agent.objects.filter(organization=organization)
        return agent


class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentPhotoUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_photo_update.html'
    form_class = PhotoAddUpdateAgentForm

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




