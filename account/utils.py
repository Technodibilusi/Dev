from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings


def create_activation_code(user):
    user.activation_code = get_random_string(10)
    user.save()


def send_activation_code(user):
    message = f"""
    Спасибо за регистрацию! Ваш код актвации {user.activation_code}
    """
    send_mail(
        subject='Активация аккаунта ',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )


def send_drop_password_code(email, code):
    message= f"""
    Введите указанный код для сброса пароля: {code}

    Если это были не Вы, то игнорируете это сообщение    
    """
    send_mail(
        subject = 'Сброс пароля',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )