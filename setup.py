from setuptools import setup
setup(name='openchiglug',
      version='1.0',
      description='ChicagoLUG website on OpenShift',
      author='Jim Campbell',
      author_email='jwcampbell@gmail.com',
      url='http://j1m.net',
      install_requires=['flask>=0.9', 'misaka>=1.0.2', 'PyYAML>=3.10',
      'gunicorn>=0.14.2'],
     )

