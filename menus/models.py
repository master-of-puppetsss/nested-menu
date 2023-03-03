from django.db import models


class Menu(models.Model):
    """ Model menu."""

    title = models.CharField(
        max_length=80,
        verbose_name='Title',
        unique=True
    )

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ['title']

    def __str__(self) -> str:
        return f'{self.title}'


class MenuItem(models.Model):
    """ Model item."""

    title = models.CharField(
        max_length=80,
        verbose_name='Title',
        unique=True
    )

    menu = models.ForeignKey(
        Menu,
        related_name='items',
        verbose_name='Menu',
        on_delete=models.CASCADE
    )

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE
    )

    url = models.CharField(
        max_length=255,
        verbose_name='Url',
        blank=True
    )

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['menu']

    def __str__(self) -> str:
        return f'{self.title}'
