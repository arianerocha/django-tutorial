from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from .forms import CommentForm

from .models import Post, About, Comment

# Uma página representando uma lista de objetos
# https://docs.djangoproject.com/pt-br/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView
class IndexView(generic.ListView):
    # Retorna o template utilizado pela view (dentro da pasta templates)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Returna Todos os Posts publicados ordenados pela data de criação, trás dos mais recentes para
        os mais antigos.
        """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Post requerido
        post = context['post']
        # Passando formulário de Comentário como parâmetro para o template
        # instanciando formulário com post relacionado;
        context['form'] = CommentForm(instance=Comment(post=post))
        # Passando uma lista de comentários aprovados de acordo com o post, como parametro para o template
        comments = Comment.objects.filter(approved_comment=True, post=post)
        context['comments'] = comments
        context['comments_count'] = comments.count()
        return context

# SOBRE MÉTODOS HTTP
# https://docs.djangoproject.com/pt-br/2.0/topics/forms/#get-and-post
def about(request):
    """
    Returna o Primeiro objeto de About.
    """
    about = About.objects.first()
    return render(request, 'blog/about.html', { 'about': about})


def comment_new(request):
    # Passa os valores inseridos no HTMl para o Form Django
    form = CommentForm(request.POST)
    #Verifica se as informações estão válidas
    post = Post.objects.get(pk=request.POST['post'])
    if form.is_valid():
        comment = form.save(commit=False)
        # salvando comentário
        comment.save()
        # adicionando mensagem de sucesso para o usuário
        messages.add_message(request, messages.INFO, 'Comentário enviado com sucesso', extra_tags='alert alert-success',)
    else:
        # adicionando mensagem de erro para o usuário
        messages.add_message(request, messages.ERROR, 'Erro ao enviar o comentário', extra_tags='alert alert-danger',)

    # Redirecionando para a view `DetailView` 
    return redirect('post-detail', permanent=True, pk=post.id)


