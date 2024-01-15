from django.core.exceptions import PermissionDenied


def user_is_recruiter(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'recruiter':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_jobseeker(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'jobseeker':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
