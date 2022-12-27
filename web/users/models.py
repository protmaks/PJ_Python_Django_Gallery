from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_img/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, ** kwargs)

        # Функция для обрезки изображения по центру.
        def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
            img_width, img_height = pil_img.size
            return pil_img.crop(((img_width - crop_width) // 2,
                                 (img_height - crop_height) // 2,
                                 (img_width + crop_width) // 2,
                                 (img_height + crop_height) // 2))

        im = Image.open(self.image.path)
        if im.height != 300 and im.width != 300:
            im_new = crop_center(im, 300, 300)
            im_new.save(self.image.path)