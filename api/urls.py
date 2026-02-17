from rest_framework.routers import DefaultRouter
from .views import TaskAPIs

router = DefaultRouter()
router.register(r'task', TaskAPIs)

urlpatterns = router.urls