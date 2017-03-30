from distutils.core import setup

package_name = 'snortunsock'
description = 'A Python listener to capture Snort event via the UNIX Socket output'

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
