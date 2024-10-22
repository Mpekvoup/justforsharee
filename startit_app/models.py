from django.db import models
from datetime import datetime
from pytils.translit import slugify


class strashno(models.Model):
    name = models.CharField("Название страшности", max_length=255)
    description = models.TextField("Описание страшности", default="Описание отсутствует")
    slug = models.SlugField(unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(verbose_name="Время создания", default=datetime.now)

    class Meta:
        verbose_name = "Страшность"
        verbose_name_plural = "Страшности"

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class slozhno(models.Model):
    name = models.CharField("Название сложности", max_length=255)
    description = models.TextField("Описание сложности", default="Описание отсутствует")
    slug = models.SlugField(unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(verbose_name="Время создания", default=datetime.now)

    class Meta:
        verbose_name = "Сложность"
        verbose_name_plural = "Сложности"

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




class age(models.Model):
    name = models.CharField("Возраст", max_length=255, unique=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возрасты"

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class parking(models.Model):
    name = models.CharField("Парковка:", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Парковка"
        verbose_name_plural = "Парковки"

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class waitroom(models.Model):
    name = models.CharField("Зона ожидания:", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Зона ожидания"
        verbose_name_plural = "Зона ожидании"

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Quest(models.Model):
    name = models.CharField("Название квеста", max_length=255)
    image_url = models.URLField("Вставьте изображение", max_length=500, default='', blank=True)
    description = models.TextField("Описание квеста", default="Описание отсутствует")
    slozhno = models.ForeignKey(slozhno, on_delete=models.CASCADE, verbose_name="Выберите сложность")
    strashno = models.ForeignKey(strashno, on_delete=models.CASCADE, verbose_name="Выберите страшность")
    age = models.ForeignKey(age, on_delete=models.CASCADE, verbose_name="Выберите возраст")
    created_at = models.DateTimeField(verbose_name="Время создания", default=datetime.now)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=1000)  


    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.created_at}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class addresesQ(models.Model):
    name = models.CharField("Название контакта", max_length=255, default="Контакты")
    image_url = models.URLField("Вставьте изображение", max_length=500, default='', blank=True)
    addres = models.CharField("Название адресса", max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=1000)  
    phone = models.CharField("Номер телефона", max_length=255)
    ostanovka = models.CharField("Название остановку", max_length=255)
    wifi = models.CharField("вай фай" , max_length=55)
    parking = models.CharField("Парковка:", max_length=55)
    waitroom = models.CharField("Зона ожидания:", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='addresses', verbose_name="Квест")


    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.pk} - {self.addres} - {self.created_at}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.addres)
        super().save(*args, **kwargs)


class infotxt(models.Model):
    title= models.CharField("Описание", max_length=500)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(verbose_name="Время создания", default=datetime.now)




    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описание"

    def __str__(self):
        return f"{self.title} - {self.created_at}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

