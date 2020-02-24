from sightengine.client import SightengineClient

client = SightengineClient('890532104', 'frvBkhp878rF3GfameWs')
output = client.check('wad').set_url('https://datatofish.com/wp-content/uploads/2019/11/001_install_python.png')
    
print(output)