from django.contrib import admin

from transaction.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'account',
        'category',
        'amount',
        'description',
        'transaction_date',
        'user_note'
    ]


admin.site.register(Transaction, TransactionAdmin)
