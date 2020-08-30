from os import path
from setuptools import setup


def get_readme(filename):
    if not path.exists(filename):
        return ''

    with open(path.join(path.dirname(__file__), filename)) as readme:
        content = readme.read()
    return content


setup(
    name='mdx_breakless_lists',
    version='1.0',
    author='adamb70',
    description='Python Markdown package extension to allow lists without a preceding empty line.',
    license='MIT',
    keywords=['markdown extension', 'markdown', 'lists'],
    url='https://github.com/adamb70/mdx-breakless-lists',
    long_description=get_readme('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['markdown>=3.0'],
    packages=['mdx_breakless_lists'],
    test_suite='mdx_breakless_lists.tests'
)
