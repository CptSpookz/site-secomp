# Controllers

> Esse diretório é um diretório de propósito geral, voltado para
> a organização do aplicativo, a saber:

### admin.py

> Procura gerenciar e autenticar a página /admin do site

### constants.py

> Utiliza constantes, atualmente primarias para o teste do banco de dados

### forms/

> Organiza os **formulários** do site, relacionados à(ao):
> * **(forms.py)** - Outras funcionaldades gerais
> * **(forms_usuario.py)** - Usuário
> * **(forms_area_admin.py)** - Área-Administrativa
> * **(forms_participante.py)** - Participante

> Estes formulários serão importados nos arquivos de imports das views

### functions/

> Reune e organiza **funções** que serão utilizadas por outros arquivos:
> * **(aux.py)** - Funções auxiliares
> * **(email.py)** - Funções de email
> * **(dictionaries.py)** - Funções que constroem dicionários para os templates
> * **(form_choices.py)** -  Funções que montam as opções de escolha dos campos de seleção dos formulários
> *  **(custom_form_validators.py)** - Funções customizadas de validação dos formulários

### urls/

> Organiza as **urls** do site em umas lista de listas com o padrão:
> > [**route:(string)**, **endpoint:(string)**, **view_func:(function)**, **methods:(list)**],

> No arquivo init, a função **main_route_controler()** recebe essa lista de urls
como parâmetro e adiciona as regras de url com o método **app.add_url_rule()** do módulo do flask

### views/

> Organiza as **views** que estarão associadas à sua respectiva rota/url no módulo **urls/**

> Estão separadas em:
> * **(views.py)** - Views associadas às páginas de informação
> * **(views_login.py)** - Views associadas às páginas de login
> * **(views_participante.py)** - Views associadas às páginas do participante e usuário
> * **(views_area_administrativa.py)** - Views associadas às páginas da área administrativa e suas funcionalidades
