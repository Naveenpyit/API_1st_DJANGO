from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

API_KEY=os.getenv('API_KEY')

class apikeycheck(BaseAuthentication):
    def authenticate(self, request):
        api_key=request.headers.get('api-key')

        if not api_key:
            return AuthenticationFailed('Key must Required')
        
        if api_key !=API_KEY:
            return AuthenticationFailed('Invalid key!')
        
        return None