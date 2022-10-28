При запуске приложения, необходимо соблюдать последоватльность миграций.
1. ./manage.py migrate accounts 0001
2. ./manage.py migrate posts 001
3. ./manage.py migrate accounts 002
4. ./manage.py migrate

