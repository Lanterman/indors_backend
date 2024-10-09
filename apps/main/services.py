from django.db import models


class HairinessChoice(models.TextChoices):
    """Choose hairiness"""

    BALD = "bald"
    LIGHT = "light-haired"
    MEDIUM = "medium-haired"
    MULTI = "multi-haired"
