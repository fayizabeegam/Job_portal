from django import template
from jobs.models import JobApplication

register = template.Library()

@register.filter(name='is_already_applied')
def is_already_applied(job, user):
    applied = JobApplication.objects.filter(job_listing=job, job_seeker=user).exists()
    return applied
