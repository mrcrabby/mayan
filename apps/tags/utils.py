from django.utils.translation import ugettext_lazy as _

from tags import tag_document_remove, tag_tagged_item_list


def get_tags_subtemplate(obj):
    """
    Return all the settings to render a subtemplate containing an
    object's tags
    """
    return {
        'name': 'generic_list_subtemplate.html',
        'context': {
            'title': _(u'tags'),
            'object_list': obj.tags.all(),
            'hide_link': True,
            'navigation_object_links': [tag_tagged_item_list, tag_document_remove],
        }
    }
