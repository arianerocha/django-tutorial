from django.contrib import admin
from django.utils import timezone

from blog.models import Post, About, Comment

# A classe ModelAdmin é a representação de um model na interface de Admin.
# https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    # ´readonly_fields´ Campo apenas para visualizar
    readonly_fields = ['published_date']
    # 'fieldsets'- Maior controle sobre o layout dos forms de admin
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        (None, {
            'classes': ['wide', 'extrapretty'],
            'fields': ['author', 'title', 'text',],
        }),
        ('Datas', {'fields': ['created_date', 'published_date']}),
    )
    
    # ´list_display´ Controle da listagem 
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('title', 'author', 'created_date', 'published_date')
    # ´list_display_links´ Controlle de quais itens serão links de edição
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display_links
    list_display_links = ('title', 'author')
    
    # Ação personalizada, chama a função 'make_published'
    actions = ['make_published']

    # função para publicar o post
    def make_published(self, request, queryset):
        # 'queryset' - lista de post selecionada
        queryset.update(published_date=timezone.now())

    make_published.short_description = "Publicar Posts Selecionados"
   
class CommentAdmin(admin.ModelAdmin):
    # 'fieldsets'- Maior controle sobre o layout dos forms de admin
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        (None, {
            'classes': ['wide', 'extrapretty'],
            'fields': ['post', 'name', 'text', 'approved_comment' ],
        }),
        ('Datas', {'fields': ['created_date']}),
    )
    
    # ´list_display´ Controle da listagem 
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('post', 'name', 'text', 'created_date', 'approved_comment')
    # ´list_display_links´ Controlle de quais itens serão links de edição
    # https://docs.djangoproject.com/pt-br/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display_links
    list_display_links = list_display
    
    # Ação personalizada, chama a função 'make_published'
    actions = ['make_published']

    # função para publicar o post
    def make_published(self, request, queryset):
        # 'queryset' - lista de post selecionada
        queryset.update(approved_comment=True)

    make_published.short_description = "Aprovar Comentários Selecionados"

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(About)

