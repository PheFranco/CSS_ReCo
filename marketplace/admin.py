from django.contrib import admin
from .models import Donation, Message

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'donor', 'city', 'condition', 'is_available', 'created_at')
    list_filter = ('is_available', 'condition', 'city')
    search_fields = ('title', 'description', 'donor__username', 'contact_email')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'donation', 'sender', 'recipient', 'has_image', 'created_at', 'read')
    list_filter = ('created_at', 'read', 'donation')
    search_fields = ('text', 'sender__username', 'recipient__username', 'donation__title')
    readonly_fields = ('created_at', 'sender', 'recipient', 'donation')
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.short_description = 'Com imagem'
    has_image.boolean = True