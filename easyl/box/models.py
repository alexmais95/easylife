from django.db import models




class Client(models.Model):
    id_by_tg = models.IntegerField(primary_key=True)
    name_tg = models.CharField("Телеграм користувача", max_length=255)
    name = models.CharField("Імя користувача", max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    language = models.CharField(default="ua")
    country = models.CharField(default="Україна")
    code_warification = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name_tg
    
    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"

class Box(models.Model):
    id_box = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    summ = models.DecimalField(max_digits=6, decimal_places=2)
    tyme_open = models.IntegerField("Кількість відкриттів", default=0)
    type_distrybushin = models.CharField(help_text="Рандомно|Рівномірно")
    summ_now = models.DecimalField(max_digits=6, decimal_places=2)
    distrybushim_now = models.CharField()
    status = models.CharField(help_text="Активно|Неактивно")
    user = models.ManyToManyField('Client', verbose_name='Клієнт', related_name='user_box')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бокс"
        verbose_name_plural = "Бокси"

class UserBox(models.Model):
    id_by_tg = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_box = models.ForeignKey('Box', on_delete=models.CASCADE)
    

class Operation(models.Model):
    id_by_tg = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_box = models.ForeignKey('Box', on_delete=models.CASCADE)
    summ = models.DecimalField(max_digits=6, decimal_places=2)
    nom_operation = models.IntegerField()
    time = models.TimeField(auto_now=True)
    status =  models.CharField(help_text="Активна|Неактивна")

    def __str__(self) -> str:
        return self.id_by_tg

    class Meta:
        verbose_name = "Операції клієнта"
        verbose_name_plural = "Операції клієнтів"

class Balance(models.Model):
    id_user = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_coin = models.ForeignKey('Coin', on_delete=models.CASCADE)

class Coin(models.Model):
    id_coin = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    numb_coin = models.IntegerField("Кількість монет")
    status =  models.CharField()
    user = models.ManyToManyField('Client', verbose_name='Монети', related_name='user_coin')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Монета"
        verbose_name_plural = "Монети"

class News(models.Model):
    id_news = models.BigAutoField(primary_key=True)
    text = models.TextField("Текст Новин")

    class Meta:
        verbose_name = "Новини"
        verbose_name_plural = "Новини"

class MassageUser(models.Model):
    id_user = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_news = models.ForeignKey('News', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)




