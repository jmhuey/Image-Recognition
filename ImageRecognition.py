from sightengine.client import SightengineClient

client = SightengineClient('890532104', 'frvBkhp878rF3GfameWs')

input_URL = input("Enter a URL to a picture: ")


output = client.check('wad').set_url(input_URL)
    
print(output)