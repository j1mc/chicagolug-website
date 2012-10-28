from setuptools import setup
setup(name='chicagolugflask',
      version='1.0',
      description='ChicagoLUG website on OpenShift',
      author='Jim Campbell',
      author_email='jwcampbell@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['flask>=0.9', 'markdown>=2.1.1', 'pyyaml>=3.10',
      'gunicorn>=0.14.2'],
     )

