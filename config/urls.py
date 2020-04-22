from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView, RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
                  path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
                  path('favicon.ico', RedirectView.as_view(url='/static/images/favicons/favicon.ico')),
                  path(settings.ADMIN_URL, admin.site.urls),
                  path("accounts/", include("allauth.urls")),
                  # Your stuff: custom urls includes go here
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# API URLS
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API base url
    path("api/core/", include("invoice_101.core.urls")),
    path("api/users/", include("invoice_101.users.urls")),
    path("api/beta/", include("invoice_101.beta.urls")),
    path("api/customer/", include("invoice_101.customer.urls")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
