# Django baby steps

![image](https://user-images.githubusercontent.com/1257048/203446738-7c15fb76-5edf-4853-bb6d-bf0d3795bc46.png)

Do you know how to put Django in a single script?

Can you deconstruct the folder structure?

Don't?

So come with me and I'll show you!

<br/><br/>

## Installation

Clone the project.

    cd your/projects/
    git clone https://github.com/devfuria/django-baby-steps.git
    cd django-baby-steps/

Launch the [virtualenv](http://www.devfuria.com.br/linux/cookbook/virtualenv/) in the current folder.

    virtualenv .

Turn on the virtual environment.

    source bin/activate

First of all, update the [pip](http://www.devfuria.com.br/linux/cookbook/pip/).

    pip install --upgrade pip

Install Django.

    python -m pip install Django
    // or
    pip install Django==4.1

Testing...

    python3 -c "import django; print(django.get_version())"

    // or

    python3 ./step-000/foo.py
    # 4.1

When you finish

    deactivate