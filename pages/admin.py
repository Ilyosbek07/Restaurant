from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from pages.models import ContactModel


class MyTranslationAdmin(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'message']
	list_filter = ['created_at']
	search_fields = ['name', 'email']
