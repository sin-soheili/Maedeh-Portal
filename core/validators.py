import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_iranian_cellphone(value):
    value = str(value).translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789'))

    pattern = r'^09\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError(_("شماره تلفن همراه معتبر نیست."))
