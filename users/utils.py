from rest_framework_simplejwt.authentication import JWTAuthentication as jwt


def get_access(self, request):
    header = jwt.get_header(self, request=request)
    if header:
        raw_token = jwt.get_raw_token(self, header)
        valid_token = jwt.get_validated_token(self, raw_token)
        return valid_token
    return header
