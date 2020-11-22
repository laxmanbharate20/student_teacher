from rest_framework.routers import SimpleRouter
from .views import StudentView,SubjectView,TeacherView
simple_router = SimpleRouter()
simple_router.register("student",StudentView)
simple_router.register("teacher",TeacherView)
simple_router.register("subject",SubjectView)

urlpatterns = simple_router.urls
