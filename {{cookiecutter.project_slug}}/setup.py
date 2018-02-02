"""{{ cookiecutter.project_name }} setup script."""

from codecs import open
from setuptools import setup, find_packages
import os

project_slug = '{{ cookiecutter.project_slug }}'
root_path = os.path.abspath(os.path.dirname(__file__))

# Get the version from the VERSION file
with open(os.path.join(root_path, project_slug, 'VERSION'),
          encoding='utf-8') as f:
    version = f.read().strip()

# Get the long description from the README file
with open(os.path.join(root_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=project_slug,
    version=version,
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,
    url='{{ cookiecutter.project_repo_url }}',
    author='{{ cookiecutter.project_author_name }}',
    author_email='{{ cookiecutter.project_author_email }}',
    license='LGPLv3+',  # XXX: update license and remove comment
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or '
        'later (LGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],  # XXX: update classifiers and remove comment
    keywords='flask wsgi web',  # XXX: update keywords and remove comment
    packages=find_packages(exclude=['docs', 'tests', 'atests']),
    py_modules=['{{ cookiecutter.project_slug }}_app'],
    install_requires=[
        'chaussette',
        'circus',
        'flask',
        'konfig',
        'six',
        'xdg<2.0',
        'html5lib<1.0.1',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'Sphinx',
            'bumpversion',
            'check-manifest',
            'flake8',
            'pytest',
            'readme_renderer',
            'tox',
        ],
        'ci': [
            'Sphinx',
            'coverage',
            'check-manifest',
            'flake8',
            'pytest',
            'pytest-cov',
            'readme_renderer',
            'robotframework',
            'robotframework-selenium2library',
            'robotframework-xvfb',
            'tox',
        ],
    },
    package_data={
        project_slug: ['VERSION'],
    },
    data_files=[
        ('examples', [
            '{{ cookiecutter.project_slug }}.ini.example',
            'circus.ini.example',
        ]),
    ],
    entry_points={
        'console_scripts': ['{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main']
    },
    scripts=[os.path.join('{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}_cli.py')],
)
