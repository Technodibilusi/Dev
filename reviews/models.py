from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class AbstractedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('article.Article', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Comment(AbstractedModel):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} from {self.user.username}"

    class Meta:
        default_related_name = 'comments'