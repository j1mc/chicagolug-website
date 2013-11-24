from setuptools import setup
setup(name='openchiglug',
      version='1.0',
      description='ChicagoLUG website on OpenShift',
      author='Jim Campbell',
      author_email='jcampbell@gnome.org',
      url='http://chicagolug.org',
      install_requires=['flask>=0.9', 'markdown==2.1.1', 'PyYAML>=3.10',
      'gunicorn>=0.14.2', 'pygments>=1.6'],
     )

