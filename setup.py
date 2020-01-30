
from distutils.core import setup
setup(
  name = 'swagger_django_generator',         # How you named your package folder (MyLib)
  packages = ['./', 'swagger_django_generator', 'swagger_django_generator.templates.django'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Convert given spec to django code',   # Give a short description about your library
  author = 'Sai Sri Vathsa Vemula',                   # Type in your name
  author_email = 'vathsa.vemula@codenation.co.in',      # Type in your E-Mail
  url = 'https://github.com/trilogy-group/swagger-django-generator',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/trilogy-group/swagger-django-generator/archive/v0.9.tar.gz',    # I explain this later on
  keywords = ['swagger', 'spec', 'django', 'converter'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
