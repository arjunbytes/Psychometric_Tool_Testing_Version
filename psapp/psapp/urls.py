# Import necessary modules
from django.contrib import admin
from django.urls import path
from authentication import views as auth_views  # Correctly import views from the authentication app
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# Define URL patterns
urlpatterns = [
    path('', auth_views.survey_view, name='home'),  # Use the survey view for the home page
    path('survey/thanks/', auth_views.survey_thanks_view, name='survey_thanks'),
    path('admin/', admin.site.urls),  # Admin interface
    path('login/', auth_views.login_page, name='login_page'),  # Login page
    path('register/', auth_views.register_page, name='register'),  # Registration page
    path('home/', auth_views.home, name='recipes'),  # Home page (if applicable)
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
