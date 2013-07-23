from setuptools import setup, find_packages

from swx_datastore import __version__

setup(
    name='swx-datastore',
    version=__version__,
    long_description="""\
""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    namespace_packages=['swx_datastore'],
    zip_safe=False,
    author='Various at ScraperWiki, Ross Jones',
    author_email='ross@mailbolt.com',
    license='AGPL',
    url='',
    description='Old ScraperWiki datastore',
    keywords='datastore scraping',
    dependency_links = ['http://github.com/rossjones/swx-common/tarball/master#egg=swx-common-0.1.0'],
    install_requires=[
        "ConcurrentLogHandler==0.8.3",
        "swx-common>=0.1"
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'ckan': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [console_scripts]
    datastore = swx_datastore.main:run_server
""",
    test_suite = 'nose.collector',
)
