import os

name = os.getenv('my_name', 'World')
print(f'Hello {name} from Python')