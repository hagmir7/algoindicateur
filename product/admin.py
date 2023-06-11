from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



@admin.register(Product)
class ProductIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Benefit)
class BenefitIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Order)
class OrderIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Contact)
class ContactIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Language)
class LanguageIMportExport(ImportExportModelAdmin):
    pass

@admin.register(Post)
class PostIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Category)
class CategoryIMportExport(ImportExportModelAdmin):
    pass