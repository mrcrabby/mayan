from django.contrib import admin

from metadata.admin import DocumentMetadataInline

from documents.models import DocumentType, Document, \
    DocumentTypeFilename, DocumentPage, \
    DocumentPageTransformation, RecentDocument


class DocumentTypeFilenameInline(admin.StackedInline):
    model = DocumentTypeFilename
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTypeAdmin(admin.ModelAdmin):
    inlines = [
        DocumentTypeFilenameInline
    ]


class DocumentPageTransformationAdmin(admin.ModelAdmin):
    model = DocumentPageTransformation


class DocumentPageInline(admin.StackedInline):
    model = DocumentPage
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        DocumentMetadataInline, DocumentPageInline
    ]
    list_display = ('uuid', 'file_filename', 'file_extension')


class RecentDocumentAdmin(admin.ModelAdmin):
    model = RecentDocument
    list_display = ('user', 'document', 'datetime_accessed')
    readonly_fields = ('user', 'document', 'datetime_accessed')
    list_filter = ('user',)
    date_hierarchy = 'datetime_accessed'


admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentPageTransformation,
    DocumentPageTransformationAdmin)
admin.site.register(RecentDocument, RecentDocumentAdmin)
