from django.db import models


class HairinessChoice(models.TextChoices):
    """Choose hairiness"""

    BALD = "BALD", "bald"
    LIGHT = "LIGHT", "light-haired"
    MEDIUM = "MEDIUM", "medium-haired"
    MULTI = "MULTI", "multi-haired"
