
from .gen.custom_fields import _CustomFields

class CustomFields(_CustomFields):
    """Custom Fields resource"""
    def add_enum_option(self, custom_field, params={}, **options):
        self.create_enum_option(custom_field, params, **options)

    def reorder_enum_option(self, custom_field, params={}, **options):
        self.insert_enum_option(custom_field, params, **options)
