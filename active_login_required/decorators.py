from __future__ import unicode_literals

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


__all__ = ('active_login_required', )


def active_login_required(function=None,
                          redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url=None):
    """Ensures that a user meets two qualifications:

    1. The user is authenticated
    2. The user is active

    Deactivating a user does not disable their session.
    (Remember that sessions aren't tied to users).
    """

    actual_decorator = user_passes_test(
        test_func=lambda u: u.is_authenticated() and u.is_active,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)

    return actual_decorator
