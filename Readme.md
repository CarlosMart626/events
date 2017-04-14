# Events
Este proyecto permite crear eventos y cada evento creado crea eventos recurrentes durante ocho meses durante las dos primeras semanas el mismo dia de la semana.

Para un primer evento el dia **2017-04-07** el cual es **viernes** crearia los siguientes eventos programados.

* 2017-05-12
* 2017-06-09
* 2017-07-14
* 2017-08-11
* 2017-09-15
* 2017-10-13
* 2017-11-10
* 2017-12-15

Donde cada evento recurrente se ubica en la segunda semana de los siguientes meses teniendo en cuenta en los casos en que el mes empece el viernes, sábado o domingo se tomará la siguiente semana. Como por ejemplo el caso **Julio** donde el mes inicia el sábado y es por esto que el evento queda programado para el **2017-07-14** quedando para el segundo viernes del mes.

### Run Project

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Run tests

```
python manage.py test
```
