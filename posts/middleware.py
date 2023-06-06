from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class CustomMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        print("---run before view")
        # Logic to be executed before the view is called
        return None  # Return None or the response object
    
    def process_response(self, request, response):
        print("---run after view")
        
        return response  # Return the response object
    
    def process_exception(self, request, exception):
        print("---run during exception")
        
        return None
