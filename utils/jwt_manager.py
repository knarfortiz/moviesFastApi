from jwt import encode, decode


def generate_jwt(payload, secret="!·$%&/()=", algorithm="HS256"):
    return encode(payload, secret, algorithm=algorithm)


def validate_jwt(token: str, secret="!·$%&/()=", algorithm="HS256"):
    return decode(token, secret, algorithms=[algorithm])
