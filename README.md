# Exemplo de crud usando Fast Api e postgres

Para rodar o projeto é necessaŕio ter instalado o docker e o docker-compose.

### Para subir o container no banco localmente

```
./bin/start_database.sh
```

### Caso seja necessário, dê permissão de execução ao script do banco

```
chmod +x bin/start_database.sh
```

### Para rodar as migrations
```
docker-compose run --rm customer_manager poetry run alembic upgrade head
```

### Para rodar os testes
```
docker-compose run --rm customer_manager poetry run pytest
```

### Link do projeto no heroku

https://customer-manager-28112021.herokuapp.com/docs