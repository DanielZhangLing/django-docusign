from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from django_docusign_demo import views


home_view = views.HomeView.as_view()
settings_view = views.SettingsView.as_view()
create_signature_view = views.CreateSignatureView.as_view()
create_signature_template_view = views.CreateSignatureTemplateView.as_view()
signer_view = views.SignerView.as_view()
signer_return_view = views.SignerReturnView.as_view()
signer_return_with_callback_view = views.SignerReturnWithCallbackView.as_view()
signer_canceled_view = views.SignerCanceledView.as_view()
signer_error_view = views.SignerErrorView.as_view()
signer_declined_view = views.SignerDeclinedView.as_view()
signer_signed_view = views.SignerSignedView.as_view()
signature_callback_view = csrf_exempt(views.SignatureCallbackView.as_view())


urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^settings/$', settings_view, name='settings'),
    url(r'^signature/add/$', create_signature_view, name='create_signature'),
    url(r'^signature/add/template/$', create_signature_template_view,
        name='create_signature_template'),
    url(
        r'',
        include(
            [
                url(r'^signer/(?P<pk>\d+)/$', signer_view, name='signer'),
                url(r'^signer/(?P<pk>\d+)/return/$',
                    signer_return_view,
                    name='signer_return'),
                url(r'^signer/(?P<pk>\d+)/return-with-callback/$',
                    signer_return_with_callback_view,
                    name='signer_return_with_callback'),
                url(r'^signer/(?P<pk>\d+)/canceled/$',
                    signer_canceled_view,
                    name='signer_canceled'),
                url(r'^signer/(?P<pk>\d+)/error/$',
                    signer_error_view,
                    name='signer_error'),
                url(r'^signer/(?P<pk>\d+)/declined/$',
                    signer_declined_view,
                    name='signer_declined'),
                url(r'^signer/(?P<pk>\d+)/signed/$',
                    signer_signed_view,
                    name='signer_signed'),
                url(r'signature/callback/$',
                    signature_callback_view,
                    name='signature_callback')
            ],
            namespace='anysign',
            app_name='anysign',
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
