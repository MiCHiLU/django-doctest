# -*- coding: utf-8 -*-
"""
>>> from django_doctest import Test
>>> from django.test.client import Client

#django_doctest.Test
>>> t = Test()
>>> t.assertResponses({"/src/render/": (200,)})
Found ... instances of 'TEMPLATE_STRING_IF_INVALID' in /src/render/ (expected 0)
>>> t = Test(invalid_string=" ")
>>> t.assertResponses({"/src/render/": (200,)})
Found ... instances of ' ' in /src/render/ (expected 0)
>>> class MyTest(Test):
...     invalid_string="Example."
>>> t = MyTest()
>>> t.assertResponses({"/src/render/": (200,)})
Found ... instances of 'Example.' in /src/render/ (expected 0)
>>> t = Test(invalid_string=False)
>>> t.assertResponses({"/src/render/": (200,)})
>>> class MyTest(Test):
...     invalid_string=False  #bool(invalid_string) is False
>>> t = MyTest()
>>> t.assertResponses({"/src/render/": (200,)})

>>> t = Test(invalid_string=False)
>>> isinstance(t.client, Client)
True
>>> t.client == t.c
True

#"URL": (status_code, "template or redirect_url"),
>>> urls = {\
 "/src/render/0": (200, ),\
 "/src/render/1": (200, ""),\
 "/src/render/2": (200, "/src/use_template/"),\
 "/src/use_template/0": (200, "use_template.html"),\
 "/src/use_template/1": (200, "sample.html"),\
 "/src/use_template/2": (200, ("use_template.html", "sample.html")),\
 "/src/render": (301, "/src/render/"),\
 "/src/render_miss": (301, "/src/render/"),\
 "/src/render/3": (404, ),\
 "/src/none/0": (404, ("404.html",)),\
 "/src/none/1": (404, ("404.html", "none", )),\
 "/src/none/2": (2000, ""),\
 "/src/none/3": ("200", ""),\
}
>>> t.assertResponses(urls)
Template '/src/use_template/' was not used to render the response. Actual template was '<Unknown Template>', in '/src/render/2'
Response didn't redirect as expected: Reponse code was 200 (expected 404), in '/src/render/3'
Response didn't redirect as expected: Reponse code was 404 (expected 301), in '/src/render_miss'
Template 'use_template.html' was not used to render the response. Actual template was 'sample.html', in '/src/use_template/2'
Template 'use_template.html' was not used to render the response. Actual template was 'sample.html', in '/src/use_template/0'
Response didn't redirect as expected: Reponse code was 404 (expected 2000), in '/src/none/2'
Bad test. '/src/none/3': ('200', '')
Template 'none' was not used to render the response. Actual template was '404.html', in '/src/none/1'

# Fixtires handling
>>> t.refresh_data("src", verbosity=1)
Reset databases...
  src.models

>>> t.refresh_data(app_label=["src"], fixtures="empty", verbosity=1)
Reset databases...
  src.models
Installing xml fixture 'empty' from '.../src/fixtures'.

>>> t = Test(fixtures=["nothing", "empty"])
>>> t.fixtures
['nothing', 'empty']
>>> t.refresh_data(verbosity=1)
Reset databases...
  django.contrib.auth.models
  django.contrib.contenttypes.models
  django.contrib.sessions.models
  django.contrib.admin.models
  src.models
Installing xml fixture 'empty' from '.../src/fixtures'.


#django_doctest
>>> from django_doctest import flush, loaddata, reset
>>> flush(verbosity=1)

#Authentication
>>> assert(t.logined == None)
>>> option = dict(\
 auth=dict(username="test", password="secret"),\
)

>>> t = Test(**option)
>>> t.logined
False

>>> loaddata("auth", verbosity=1)
Installing json fixture 'auth' from '.../src/fixtures'.
Installed 1 object(s) from 1 fixture(s)

>>> t = Test(**option)
>>> t.logined
True
>>> t.logout()
>>> assert(t.logined == None)
>>> t.login()
>>> t.logined
True
>>> t.logout()
>>> assert(t.logined == None)
>>> t.login(auth=dict(username="test", password="none"))
>>> t.logined
False

>>> reset(verbosity=1)
Reset databases...
  django.contrib.auth.models
  django.contrib.contenttypes.models
  django.contrib.sessions.models
  django.contrib.admin.models
  src.models

#etc
>>> from django_doctest import to_iter
>>> to_iter(None)
>>> to_iter(str("s"))
('s',)
>>> to_iter(list("l",))
['l']
>>> to_iter(tuple("t",))
('t',)
>>> to_iter(dict(key = "d"))
{'key': 'd'}

#teardown
>>> flush()
"""
