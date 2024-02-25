import re
from rest_framework.serializers import ValidationError

class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        data_link = "youtube.com"
        tmp_value = dict(value).get(self.field)
        if tmp_value != None and not data_link in tmp_value:
            raise ValidationError('Link is not OK')
