from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from active_login_required import active_login_required


@active_login_required
def test_view_a(request):
    return HttpResponse(settings.AFFIRMATIVE)
