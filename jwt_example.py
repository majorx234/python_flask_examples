#!/usr/bin/env python3

import sys
import jwt

def sign_user(user, jwt_secret):
    payload = {"user":user}
    token = jwt.encode(payload, jwt_secret, algorithm="HS256")
    return token

if __name__ == '__main__':
    user = sys.argv[1]
    jwt_secret = sys.argv[2]
    token = sign_user(user, jwt_secret)
    print("{}".format(token))
