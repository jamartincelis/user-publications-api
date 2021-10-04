#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply make migrations only develop"
#python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Loaddata database fixtures"
python manage.py loaddata user/fixtures/users.yaml
python manage.py loaddata catalog/fixtures/codetype.yaml
python manage.py loaddata catalog/fixtures/accounts_types.yaml
python manage.py loaddata catalog/fixtures/transactions_categories.yaml
python manage.py loaddata transaction/fixtures/transactions.yaml
python manage.py loaddata budget/fixtures/budgets.yaml
python manage.py loaddata faq/fixtures/faqs.yaml

echo "Start server in dev mode"
python manage.py runserver 0.0.0.0:8000

# exec "$@"