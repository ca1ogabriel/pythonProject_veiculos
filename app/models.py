from django.db import models

from djmoney.models.fields import MoneyField

from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

from django.db.models.functions import Lower

YESNO_CHOISES = (
    (True, 'Sim'),
    (False, 'Não')
)
MAKE_CHOICES=(
    (1, 'Fiat'),
    (2, 'Chevrolet'),
    (3, 'Ford'),
    (4, 'Toyota'),
)
class modeloVeiculo(models.Model):
    nome = models.CharField(
        verbose_name='modelo',
        max_length=75,
        unique=True,
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = 'Modelo do veículo',
        verbose_name_plural = 'Modelos do veículo',
        ordering = ['-nome']
        indexes=[
            models.Index(fields=['nome']),
            models.Index(
                fields=['-nome'],
                name='desc_name_idx',
            ),
            models.Index(
                Lower('nome').desc(),
                name='lower_name_idx'
            )
        ]


class motor(models.Model):
    nome = models.CharField(
        verbose_name='Motorização',
        max_length=75,
        blank=True,
        null=True
    )
    modelo_veiculo = models.ForeignKey(
        modeloVeiculo,
        on_delete=models.CASCADE,
        verbose_name='Modelo',
        related_name='modelo_motor',
        blank=True,
        null=True
    )


class veiculo(models.Model):
    niv = models.CharField(
        verbose_name='niv',
        max_length=17,
        unique=True,
        null=True
    )
    venda = models.BooleanField(
        verbose_name='vendido?',
        choices=YESNO_CHOISES,
        default=False,
        blank=True,
        null=True
    )
    preco = MoneyField(
        max_length=19,
        decimal_places=2,
        max_digits=15,
        default_currency='USD',
        null=True,
        validators=[
            MinMoneyValidator(
                {'EUR': 500, 'USD': 400}
            ),
            MaxMoneyValidator(
                {'EUR': 500000, 'USD': 400000}
            )
        ]
    )
    modelo_veiculo = models.ForeignKey(
        modeloVeiculo,
        on_delete=models.CASCADE,
        verbose_name='Modelo',
        related_name='modelo_veiculo',
        blank=True,
        null=True
    )
    motor = models.ForeignKey(
        motor,
        on_delete=models.CASCADE,
        verbose_name='Motor',
        related_name='Motor_veiculo',
        blank=True,
        null=True,
    )
    make = models.PositiveIntegerField(
        choices=MAKE_CHOICES,
        verbose_name='Fabricante/Marca do veiculo',
        blank=True,
        null=True,
    )
class Vendedor(models.Model):
    nome = models.CharField(
        verbose_name="O nome do vendedor",
        max_length=150,
        blank=True,
        null=True,
    )
    veiculo = models.ManyToManyField(
        veiculo,
        verbose_name='Veiculo',
        related_name='Vendedor_veiculo',
        related_query_name='Vendedore_veiculo',
        blank=True,
    )
class Engine2(models.Model):
    nome = models.CharField(
        verbose_name='Engine',
        max_length=75,
        blank=True,
        null=True
    )
    tipo = models.CharField(
        max_length=155,
        null=True
    )

    class Meta:
        db_table = 'app_pratica_engine'

class Pessoa(models.Model):
    nome = models.CharField(
        max_length=155
    )
    sobrenome = models.CharField(
        max_length=155,
        null=True
    )
