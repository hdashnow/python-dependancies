from dependencies import extract_package
import xmlrpc.client as xmlrpclib

import random
client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
packages = ['gala', 'scikit-learn', 'scipy', 'scikit-image', 'Flask']
random.shuffle(packages)
for i, package in enumerate(packages):
    extract_package(package, to='test-pypi-deps.txt',
                    client=client, n=i)
