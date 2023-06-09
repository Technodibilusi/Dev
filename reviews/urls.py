from rest_framework import routers

from .views import CommentViewSet


router = routers.DefaultRouter()
router.register('comment', CommentViewSet, 'comment')


urlpatterns = router.urls