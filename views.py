from datetime import datetime

from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

#change your model
from .models import Jobs


class HomeJobs(TemplateView):
    #template name
    template_name = 'jobs/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeJobs, self).get_context_data(**kwargs)
        page_number = self.request.GET.get('page') #get page number
        get_datetime = datetime.now()
        get_date = get_datetime.strftime('%Y-%m-%d')
        cnv_date = datetime.strptime(get_date, '%Y-%m-%d').date()

        # select all retrieve data in database
        jobs_query = Jobs.objects.all()

        lst = []
        for get_datetime in jobs_query:
            jobs_deadline = get_datetime.deadline_job

            if cnv_date < jobs_deadline:
                """ show deadline job active in home page"""
                lst.append(get_datetime)

        paginate  = Paginator(lst, 1)

        try:
            jb = paginate.page(page_number)
        except PageNotAnInteger:
            jb= paginate.page(1)
        except EmptyPage:
            jb = paginate.page(paginate.num_pages)

        context['jobs'] = jb
        return context
