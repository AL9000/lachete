from blog.models import Article, Categorie, Commentaire
from django.views import generic
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse


class IndexView(generic.ListView):
    queryset = Article.objects.published()
    model = Article
    template_name = 'blog/index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.distinct()
        context['index'] = True
        return context


class CategorieView(IndexView):
    def get_queryset(self):
        categorie = get_object_or_404(Categorie, nom=self.kwargs['categorie'])
        return Article.objects.filter(categorie=categorie)

    # TOFIX Bon, là c'est pas supersuper, je répete ce que j'ai fait pour l'indexview ...
    # J'aurais aimé garder le context de mon index view et juste filer 'categorie' en plus.
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.distinct()
        context['index'] = False
        context['categorie'] = self.kwargs['categorie']
        return context


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.distinct()
        return context


class CommentaireCreate(generic.CreateView):
    model = Commentaire
    fields = ['titre', 'contenu']

    def get_success_url(self):
        return reverse("blog:detail", kwargs={"slug": self.kwargs['slug']})

    def form_valid(self, form):
        commentaire = form.save(commit=False)
        commentaire.article = get_object_or_404(Article, slug=self.kwargs['slug'])
        commentaire.utilisateur = self.request.user
        commentaire.save()
        return HttpResponseRedirect(self.get_success_url())