from django.conf.urls import patterns, url

urlpatterns = patterns('craneui.views',
    url(r'^buildos/$', 'build_os',
        name='craneui.build_os'),
    url(r'^buildinterpreter/$', 'build_interpreter',
        name='craneui.build_interpreter'),
    url(r'^buildapplication/$', 'build_application',
        name='craneui.build_application'),
    url(r'^buildthird/$', 'build_third',
        name='craneui.build_third'),
    url(r'^versions/$', 'versions',
        name='craneui.versions'),
    url(r'^extensions/$', 'extensions',
        name='craneui.extensions'),
)
