from functools import cached_property

class Client:
    def __init__(self) -> None:
        print("Setting up the Client...")
        
    def query(self, **kwargs):
        print("Querying...", kwargs)
        
class Server:
    @property
    def client(self):
        return Client()
    
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
    
class ManualCacheManager:
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = Client()
        return self._client
    
class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
    
manager = CachedPropertyManager()
manager.perform_query(object_id = 42)
manager.perform_query(name_i_like = "%Python%")
del manager.client
manager.perform_query(age_gte = 18)