from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image as IMG

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'gallery_img/user_{0}/{1}'.format(instance.author.id, filename)

class Image(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(default='default_gallery.jpg', upload_to=user_directory_path)
    peoples = models.ManyToManyField(User, related_name='peoples', blank=True, null=True)
    geo_location = models.ManyToManyField('Country', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Функция для обрезки изображения по центру.
        def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
            img_width, img_height = pil_img.size
            return pil_img.crop(((img_width - crop_width) // 2,
                                 (img_height - crop_height) // 2,
                                 (img_width + crop_width) // 2,
                                 (img_height + crop_height) // 2))

        im = IMG.open(self.picture.path)
        if im.height != 556 and im.width != 900:
            im_new = crop_center(im, 900, 556)
            im_new.save(self.picture.path)


class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name