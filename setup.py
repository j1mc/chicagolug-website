from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='chicagolug',
      version='1.2',
      description='ChicagoLUG website on OpenShift',
      author='Jim Campbell',
      author_email='jwcampbell@gmail.com',
      url='http://j1m.net',
      install_requires=['flask>=0.9', 'misaka>=1.0.2', 'PyYAML>=3.10',
      'gunicorn>=0.14.2', 'flask_bootstrap'],
     )

