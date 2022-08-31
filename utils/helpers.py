import os
import uuid
import random
import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files import File
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


ONE_MB = 1024 * 1024


def random_with_n_digits(seed: int) -> int:
    random.seed(seed)
    range_start = 1000000000  # 10**(n-1)
    range_end = 2147483647  # (10**n)-1
    return random.randint(range_start, range_end)


def token_factory():
    return uuid.uuid4().hex


def sub_factory() -> int:
    seed: int = abs(int.from_bytes(uuid.uuid1().bytes, byteorder='big', signed=False))
    sub = random_with_n_digits(seed)
    bit_length = sub.bit_length()
    return sub >> ((bit_length - 32) if bit_length >= 32 else 0)


def file_upload_validator(value: File):
    if value.size > ONE_MB:
        raise ValidationError(
            _('File size must be lower than 1MB'),
            params={'value': value},
        )

    return None


def file_upload_directory(instance, filename: str) -> str:
    model_name = instance.__class__.__name__
    _uuid = uuid.uuid4()
    instance_uuid = instance.id
    try:
        name: str = instance.name
        name = name.split('.')[0]
    except AttributeError:
        name: str = ''
    now_time = timezone.now()
    year = now_time.year
    month = now_time.month
    day_number = now_time.day
    date_directory = '{0}/{1}/{2}'.format(year, month, day_number)
    time = now_time.time()
    return settings.UPLOAD_DIRECTORY + '/' + model_name + '/' + str(instance_uuid) + '/' + date_directory + '/' + str(
        time).replace(':', '_') + '_' + str(_uuid) + '_' + name + '.' + filename.split('.')[-1]


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
