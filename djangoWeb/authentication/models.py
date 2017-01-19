from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # 通过user与User建立起一对一的映射关系，
    # 在使用时 user 是一个 User 对象，user.person 可以获得对应的 Person 对象
    user = models.OneToOneField(User)
    url = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    picture_url = models.CharField(max_length=120, null=True, blank=True)

    def get_url(self):
        url = self.url
        if not self.url.startswith("http://") \
                and not self.url.startswith("https://") \
                and len(self.url) > 0:
            url = "http://" + str(self.url)
        return url

    def get_picture(self):
        if not self.picture_url:
            no_picture = '/static/img/user.png'
            return no_picture

        return self.picture_url

    def get_screen_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()


# 基本上无论什么时候保存事件（Save事件）发生，create_user_profile和save_user_profile方法都会被信号
# 连接到用户模型。这种信号被称为post_save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)
