## Flask Example
* installation: 
```
python3 -m venv env 
source env/bin/activate
pip install flask flask_cors flask_restx jwt
```

* run: 
```
python main.py
```

* test: 
```
curl --request GET "http://localhost:5000/persons_endpoint"
```

## Misc
* create webtoken (not in use yet)
* create jwt_secret:
** ```export JWT_SECRET=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)```
* create toke for user:
** ```python jwt_example.py $JWT_SECRET myuser```