from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Plan_It_Teknoy import views

app_name = 'Plan_It_Teknoy'

urlpatterns = [

    # Start of user pages
    path('', views.home, name="Home"),
    path("About/", views.about, name="About"),
    path("Contact/", views.contactView.as_view(), name="contact_view"),
    path("SignIn/", views.SignInView.as_view(), name="signin_view"),
    path("SignUp/", views.SignUpView.as_view(), name="signup_view"),
    path("SignUpTeacher/", views.SignupTeacherView.as_view(), name="signupT_view"),
    # Select Role url
    path("SelectRole/", views.SelectRoleView.as_view(), name="select_view"),
    # End of user pages

    # # icon browser tab
    # path("favicon.ico", RedirectView.as_view(
    #     url=staticfiles_storage.url("favicon.ico"))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
