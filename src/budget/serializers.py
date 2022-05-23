from rest_framework import serializers

from budget.models import Budget
from django.conf import settings

class BudgetSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un presupuesto.
    """
    class Meta:
        model = Budget
        exclude = [
            'status'
        ]

    transaction_type_catalogs = settings.TRANSACTION_TYPE_CATALOGS

    def get_object_category(self, category_id):
        """
        Busca en el diccionary en memory el objeto relacionado con el id de la
        Category
        """
        try:
            r = self.transaction_type_catalogs[str(category_id)]
        except TypeError:
            r = self.transaction_type_catalogs[(str(category_id))]
        except KeyError:
            r = self.transaction_type_catalogs
        return r

    def to_representation(self, instance):
        """
            Permite alterar la representacion del modelo de Transaction
            para `pegar` un objecto del modelo de Category de modo que el front
            reciba el paquete completo
        """
        data = super(BudgetSerializer, self).to_representation(instance)
        # Reviso categoria ya que es un campo que puede ser nulo
        if data['category'] is None:
            # indica que una transacción tiene valor nulo como categoría
            data['category'] = self.get_object_category('f37b6770-7fc5-43e0-a837-50926e1ee459')
            data.update(data)
        else:
            data['category'] = self.get_object_category(data['category'])
            data.update(data)

        return data
