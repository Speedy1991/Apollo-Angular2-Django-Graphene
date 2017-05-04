## Django GraphQL Server

```python
pip3 install -r requirements            # Install requirements
python3 manage.py makemigrations        # Prepare db changes/creation
python3 manage.py migrate               # Write migrations to the db
python3 manage.py loaddata init.yaml    # Fill db with dummydata
python3 manage.py runserver             # Starts the server on localhost:8000
```

### Logins

```bash
Login: admin
Password: admin2017
```

### URLs
```bash
http://localhost:8000/api               # Api
http://localhost:8000/api/graphiql      # GraphiQL
```

License
-------
MIT
