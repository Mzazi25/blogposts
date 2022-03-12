import urllib.request,json
from .models import Blog, Quotes

# Getting the Blog base url
QUOTES_BASE_URL = None

def configure_request(app):
    global QUOTES_BASE_URL
    QUOTES_BASE_URL = app.config['QUOTES_BASE_URL']
    
def get_random_quotes():
    '''
    Function that returns json response to url request
    '''
    get_random_quotes_url = QUOTES_BASE_URL
    print(get_random_quotes_url)
    with urllib.request.urlopen(get_random_quotes_url) as url:
        get_random_quotes_data = url.read()
        get_random_quotes_response = json.loads(get_random_quotes_data)
        
        quotes_result =None
        
        author = get_random_quotes_response.get('author')
        quote = get_random_quotes_response.get('quote')
        
        
        random_quote_object = Quotes(author, quote)
    return random_quote_object
   
         