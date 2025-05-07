from django.db import models

class Gorev(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Başlık")
    aciklama = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    tamamlandi = models.BooleanField(default=False, verbose_name="Tamamlandı mı?")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.baslik
