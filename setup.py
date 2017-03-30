from distutils.core import setup

package = __import__(package_name)

package_version = package.__version__

setup(
    name='snortunsock',
    version='1.1',
    packages=['snortunsock'],
    url='',
    license='',
    author='jockdarock',
    author_email='',
    description='Trying to fix this setup file'
)
