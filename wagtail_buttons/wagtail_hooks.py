"""Draftail hooks.

Adds a .css file to the /admin/ and register a Block Element for Draftail.
"""
from django.conf import settings
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.core import hooks

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html


@hooks.register('register_rich_text_features')
def register_button_section_feature(features):
    """Register the button-block with Draftail."""

    feature_name = 'button-block'
    type_ = 'button-block'
    tag = 'div'

    control = {
        'type': type_,
        'label': ' ',
        'description': 'Button Section',
        'element': 'div',
        'icon': 'icon icon-grip',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {tag: BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'div', 'props': {'class': 'rich-text-buttons'}}}},
    })

    if hasattr(settings, 'APPEND_BUTTON_BLOCK') and getattr(settings, 'APPEND_BUTTON_BLOCK', False):
        # Auto append feature to Draftail
        features.default_features.append('button-block')


# Register a custom css file for the wagtail admin.
@hooks.register('insert_global_admin_css', order=100)
def global_admin_css():
    """Add /static/css/button-block.css to the Wagtail /admin/."""
    return format_html('<link rel="stylesheet" href="{}">', static('css/button-block.css'))
