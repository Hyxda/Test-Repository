from exencoder import Country
import json

class CountryDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_country =  Country(
            o.get('name'), 
            o.get('population'), 
            o.get('languages'),
        )
        return decoded_country

with open('canada.json','r') as f:
    country_object = json.load(f, cls=CountryDecoder)

print(type(country_object))