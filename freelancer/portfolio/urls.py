from django.urls import path

from . import views

app_name = "freelancer"

urlpatterns = [
    path('services/', views.services, name="services"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('case-studies/', views.case_studies, name="case_studies"),
    path('blog/', views.blog, name="blog"),
    path('pricing/', views.pricing, name="pricing"),
]