# Django baby steps

...Django em doses homeopáticas!


### Instalação

Clone o projeto.

    cd seus/projetos/
    git clone https://github.com/devfuria/django-baby-steps.git
    cd django-baby-steps/

Inicie o [virtualenv](http://www.devfuria.com.br/linux/cookbook/virtualenv/) na pasta atual.

    virtualenv .

Ative o ambiente virtual.

    source bin/activate

Antes de tudo, atualize o [pip](http://www.devfuria.com.br/linux/cookbook/pip/).

    pip install --upgrade pip

Instale o Django.

    python -m pip install Django
    // or
    pip install Django==4.1

Testando...

    python3 -c "import django; print(django.get_version())"

    // or

    python3 ./step-000/foo.py
    # 4.1