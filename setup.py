from setuptools import setup, find_packages

from swx.datastore import __version__

setup(
    name='swx-datastore',
    version=__version__,
    long_description="""\
""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    namespace_packages=['swx', 'swx.datastore'],
    zip_safe=False,
    author='Various at ScraperWiki, Ross Jones',
    author_email='ross@mailbolt.com',
    license='AGPL',
    url='',
    description='Old ScraperWiki datastore',
    keywords='datastore scraping',
    install_requires=[
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'ckan': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [console_scripts]
    datastore = swx.datastore.main:run_server
""",
    test_suite = 'nose.collector',
)
