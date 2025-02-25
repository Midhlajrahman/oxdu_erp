from core.base import BaseModel

from django.db import models
from django.urls import reverse_lazy



class State(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name




