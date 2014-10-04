# django-active-login-required

Yeah, it has a long name. It's useful, though.

Django's `login_required` decorator does not verify
that an authenticated user is still an active user.
This decorator will boot any deactivated users.

This decorator is simply an extention of the `login_required`
decorator, swapping out the authentication test.

Warning: deactivated user sessions are not deleted,
as Django's out-of-box sessions are not tied
to its users.

## Installation

Install from Pip:

```shell
$ pip install django-active-login-required
```

or, clone this repo.

## Usage

Simply decorate your views (or class-based views via
`method_decorator`ing `dispatch`) with the
`active_login_required` view.

Make sure you've got `LOGIN_URL` set.

```python
from active_login_required import active_login_required


@active_login_required
def my_view(request, ...):
    return ...
```

## Testing

Take the tests for a run by grabbing this repo and
installing `py.test` via `requirements.txt`.

Then simply

```shell
$ py.test
```

Presently, this has been tested with Django >= 1.6.

You can also run `tox` if you feel so inclined.

## Contributing

Something wrong? Open an issue on this repo
or shoot me a pull request with tests
and we'll get it sorted out ASAP.

## Contributing something other than code

If you just want to say thanks, I suggest doing something
donating to the [Ada Initiative](https://adainitiative.org/donate/)
or [fostering an elephant](https://www.sheldrickwildlifetrust.org/asp/fostering.asp).
