import os
import sys

from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# reading requirements
install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]
sys.path.insert(0, os.path.dirname(__file__))
version = '0.0'
setup(
    name='domnibus',
    version=version,
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    license='MIT',
    description='Get all possible information about a domain',
    keywords = ['domnibus', 'domni', 'whois', 'ssl', 'nameserver', 'dns'],
    url='https://github.com/cyriac/domnibus',
    download_url = 'https://github.com/cyriac/domnibus/archive/v{version}.tar.gz'.format(version=version),
    entry_points='''
        [console_scripts]
        domni=domnibus.cli:cli
    '''
)
