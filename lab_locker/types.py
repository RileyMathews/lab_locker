from typing import TypeGuard
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser

AuthUnion = AbstractBaseUser | AnonymousUser

def is_authenticated_user(u: AuthUnion) -> TypeGuard[AbstractBaseUser]:
    return u.is_authenticated          # runtime check ↑, static info ↓

