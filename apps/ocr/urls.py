from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ocr.views',
    url(r'^(?P<document_id>\d+)/submit/$', 'submit_document', (), 'submit_document'),
    url(r'^ocr/queue/document/list/$', 'queue_document_list', (), 'queue_document_list'),
    url(r'^ocr/queue/document/(?P<queue_document_id>\d+)/delete/$', 'queue_document_delete', (), 'queue_document_delete'),
    url(r'^ocr/queue/document/multiple/delete/$', 'queue_document_multiple_delete', (), 'queue_document_multiple_delete'),
    url(r'^ocr/queue/document/(?P<queue_document_id>\d+)/re-queue/$', 're_queue_document', (), 're_queue_document'),
    url(r'^ocr/queue/document/multiple/re-queue/$', 're_queue_multiple_document', (), 're_queue_multiple_document'),

    url(r'^ocr/queue/(?P<document_queue_id>\d+)/enable/$', 'document_queue_enable', (), 'document_queue_enable'),
    url(r'^ocr/queue/(?P<document_queue_id>\d+)/disable/$', 'document_queue_disable', (), 'document_queue_disable'),

    url(r'^ocr/document/all/clean_up/$', 'all_document_ocr_cleanup', (), 'all_document_ocr_cleanup'),
    url(r'^ocr/node/active/list/$', 'node_active_list', (), 'node_active_list'),
)
