from django.contrib import admin
from .models import Certificate, CV, Project, ProfileInfo

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title']

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at']
    list_editable = ['is_active']
    search_fields = ['title']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_featured','created_at']
    list_editable = ['order', 'is_featured']
    search_fields = ['title', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technologies', 'project_url')
        }),
        ('Files', {
            'fields': ('image', 'pdf_file', 'additional_files'),
            'description': 'Upload project files (images, PDFs, documents)'
        }),
        ('Settings', {
            'fields': ('order', 'is_featured')
        }),
    )

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Has Image'

    def has_pdf(self, obj):
        return bool(obj.pdf_file)

    has_pdf.boolean = True
    has_pdf.short_description = 'Has PDF'

@admin.register(ProfileInfo)
class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key']
