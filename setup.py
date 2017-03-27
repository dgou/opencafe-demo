from setuptools import setup, find_packages


requires = open('pip-requires').readlines()
setup(
    name='opencafe-demo',
    version='0.0.1',
    description=(
        'This is a working demo of an OpenCafe-based test suite.'),
    long_description=open('README.md').read(),
    author='Daryl Walleck',
    author_email='dwalleck@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',))