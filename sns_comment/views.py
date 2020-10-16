import logging

from django.shortcuts import render
from django.views.generic import ListView

from sns.models import SnsComment

logger = logging.getLogger(__name__)


class SnsIndexView(ListView):
    model = SnsComment
    # template_name =
