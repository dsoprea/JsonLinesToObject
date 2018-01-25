import os
import setuptools

_APP_PATH = os.path.dirname(__file__)
_RESOURCES_PATH = os.path.join(_APP_PATH, 'jlto', 'resources')

with open(os.path.join(_RESOURCES_PATH, 'README.rst')) as f:
    _LONG_DESCRIPTION = f.read()

with open(os.path.join(_RESOURCES_PATH, 'requirements.txt')) as f:
    _REQUIREMENTS = [s.strip() for s in f if s.strip() != '']

with open(os.path.join(_RESOURCES_PATH, 'version.txt')) as f:
    _VERSION = f.read().strip()

setuptools.setup(
    name='json_lines_to_object',
    version=_VERSION,
    description="Convert raw lines to a JSON object.",
    long_description=_LONG_DESCRIPTION,
    classifiers=[],
    keywords='json',
    author='Dustin Oprea',
    author_email='myselfasunder@gmail.com',
    url='https://github.com/dsoprea/JsonLinesToObject',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'jlto': [
            'resources/README.rst',
            'resources/requirements.txt',
        ],
    },
    install_requires=_REQUIREMENTS,
    scripts=[
        'jlto/resources/scripts/jlto',
    ],
)
