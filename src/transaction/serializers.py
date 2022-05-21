from os import environ

import requests

from rest_framework import serializers

from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        core_url = environ.get('CORE_SERVICE_URL')
        path = '{}users/{}/'.format(core_url,data['user'])
        r = requests.get(path, timeout=5)
        if r.status_code == 404:
            raise serializers.ValidationError("Usuario invalido")
        return data

    def to_internal_value(self, data):
        """
        Permite inicializar los valores de la peticion
        """
        data['user'] = self.context.get('request').parser_context['kwargs']['user']
        if 'category' in data:
            data['category_id'] = data['category']
        return super().to_internal_value(data)

    def get_object_category(self, category_id):
        """
        Busca en el diccionary en memory el objeto relacionado con el id de la
        Category
        """
        try:
            category = self.transaction_type_catalogs[str(category_id)]
        except TypeError:
            category = self.transaction_type_catalogs[(str(category_id))]
        except KeyError:
            category = self.transaction_type_catalogs['f37b6770-7fc5-43e0-a837-50926e1ee459']
        return category

    def to_representation(self, instance):
        """
            Permite alterar la representacion del modelo de Transaction
            para `pegar` un objecto del modelo de Category de modo que el front
            reciba el paquete completo
        """
        data = super(TransactionSerializer, self).to_representation(instance)
        # Reviso categoria ya que es un campo que puede ser nulo
        if data['category'] is None:
            # indica que una transacción tiene valor nulo como categoría
            data['category'] = self.get_object_category('f37b6770-7fc5-43e0-a837-50926e1ee459')
            data.update(data)
        else:
            data['category'] = self.get_object_category(data['category'])
            data.update(data)

        return data
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class TransactionSummarySerializer(serializers.Serializer):
    """
    Permite acceder al monto total de transacciones por categoria.
    """
    total_spend = serializers.IntegerField()
    num_transaction = serializers.IntegerField()


class MonthlyBalanceSerializer(serializers.Serializer):
    """
    Permite acceder al balance mensual por anio.
    """
    month_name = serializers.CharField()
    incomes = serializers.IntegerField()
    expenses = serializers.IntegerField()
    balance = serializers.IntegerField()
    year = serializers.CharField()
