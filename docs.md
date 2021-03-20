# Documents


## Serializer

 - [Restframework serializer](https://www.vinta.com.br/blog/2018/django-rest-framework-read-write-serializers/)

They're used to convert the data sent in a HTTP request to a Django object and a Django object to a valid response data. It looks a lot like a Django Form, but it is also concerned in defining how the data will be returned to the user. There's also the ModelSerializer, which works like a ModelForm: it uses one of your models as a basis to create its fields and its validation.


Serializers are used for “translating” Django models into other formats like XML, json, yaml(YAML Ain’t a Markup Language)

the first argument will be the format we want to serialize the data and second will be a QuerySet to serialize.

we can also translate using a serializer object directly

```
XMLSerializer = serializers.get_serializer("xml")

xml_serializer = XMLSerializer()

xml_serializer.serialize(queryset)

data = xml_serializer.getvalue()


```

The main function of serializers is to render the available information into formats that can be easily accessible and utilised by the frontend.

“Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.”



You will often use ModelSerializers as these interact directly with a model and query set.

```
from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        comment = Comment(email=’leila@example.com’, content=’foo bar’)

        from rest_framework import serializers
        
        class CommentSerializer(serializers.Serializer):
            email = serializers.EmailField()
            content = serializers.CharField(max_length=200)
            created = serializers.DateTimeField()
            serializer = CommentSerializer(comment)

            serializer.data
            
# {‘email’: ‘leila@example.com’, ‘content’: ‘foo bar’, ‘created’: ‘2016–01–27T15:17:10.375877’}

```

At this point we’ve translated the model instance into Python native datatypes. To finalise the serialization process we render the data into json.

```
from rest_framework.renderers import JSONRenderer
json = JSONRenderer().render(serializer.data)

json


# b’{“email”:”leila@example.com”,”content”:”foo bar”,”created”:”2016–01–27T15:17:10.375877"}’

```


- [When to use get_queryset()](https://medium.com/@hassanraza/when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a)

> get_queryset()

Used by ListViews - it determines the list of objects that you want to display. By default it will just give you all for the model you specify. By overriding this method you can extend or completely replace this logic. 

```
class FilteredAuthorView(ListView):
    template_name = 'authors.html'
    model = Author    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(name__startswith=self.kwargs['name'])
```


> get_context_data()

This method is used to populate a dictionary to use as the template context. For example, ListViews will populate the result from get_queryset() as author_list in the above example. You will probably be overriding this method most often to add things to display in your templates.

```
def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['page_title'] = 'Authors'
    return data
```