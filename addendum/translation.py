from modeltranslation.translator import translator, TranslationOptions

from .models import Snippet

class AddendumTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Snippet, AddendumTranslationOptions)

