# Django Course

Projeto demonstração da aula de Introdução ao Django.

## Getting Started

Para rodar o blog lembre-se de ativar seu virtualenv.

* [trabalhando-com-o-virtualenv](https://tutorial.djangogirls.org/pt/django_installation/#trabalhando-com-o-virtualenv) - Tutorial djangogirls



### Pré-requisitos

Para rodar o projeto você irá precisar de

```
Python 3.5
Django 2.0.6
```

### Instalando

Caso ainda não tenha as dependências acima, com o seu virtualenv ativado
execute a linha de comando abaixo.

```
pip install -r requirements.txt
```

> Sobre Como usar o pip
> * [Instalando o Django](https://tutorial.djangogirls.org/pt/django_installation/#instalando-o-django) - Tutorial djangogirls



Após concluir a instalação, execute os seguintes comandos:

para criar o banco de dados.
```
python manage.py migrate
```

para criar um super usuário
```
python manage.py createsuperuser
```

para rodar o servidor
```
python manage.py runserver
```


## Iniciando a Aplicação

Entre em:
```
http://127.0.0.1:8000/admin
```

 - Conclua o cadastro de usuário, preencha o nome completo.
 - Insira Posts novos.
 - Volte para a tela inicial

```
http://127.0.0.1:8000
```


## Links

* [djangogirls](https://tutorial.djangogirls.org/pt/django/) - Tutorial djangogirls
* [Django](https://www.djangoproject.com/) - Django Docs
* [Banco de dados](https://www.devmedia.com.br/bancos-de-dados-relacionais/20401) - Sobre banco de dados relacionais.
* [devmedia](https://www.devmedia.com.br/bancos-de-dados-relacionais/20401) - Sobre banco de dados relacionais.
* [wikibooks](https://pt.wikibooks.org/wiki/SQL/Banco_de_dados_Relacional) - Sobre banco de dados relacionais.
* [awesome-django](https://github.com/rosarior/awesome-django) - Projetos Django

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details
