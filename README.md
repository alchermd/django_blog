# Django Blog

A code along with Corey Schafer's [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Notes

- The Django templating system is quite similar to Twig and Jinja2.
- `{% url 'view_name' %}` is used to generate a url for a specific view.

```djangotemplate
<a href="{% url 'blog_home' %}">Django Blog</a>
```

- On that note, Django is implemented as `MVT` or Model-View-Template.
- This is essentially the same as `MVC`, just that the views are called templates and the controllers are called views.
- As for static assets, the `{% static 'path/to/asset' %}` directive is used. 

```djangotemplate
{% load static %} <!-- Load the static directive before using -->
<script src="{% static 'blog/app.js' %}"></script>
```

## License

Released under the [MIT License](LICENSE)