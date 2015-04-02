from sondages.views import IndexView


class HomeView(IndexView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['path'] = context.get('path')
        return context