from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
    (r'^render/(.*/)?', views.render),
    (r'^use_template/(.*/)?', views.use_template),
)
