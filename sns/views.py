import logging

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from sns.models import Sns

logger = logging.getLogger(__name__)


# @login_required
class SnsIndexView(ListView):
    model = Sns
    template_name = 'sns/index.html'
    paginate_by = 3
    logger.info('-- sns view index ---')
