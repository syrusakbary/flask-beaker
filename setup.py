'''
    Flask-Beaker
    ------------
    
    Beaker session interface for Flask.
'''

from setuptools import setup

setup(
    name='Flask-Beaker',
    version='0.2.0',
    url='https://github.com/syrusakbary/flask-beaker',
    license='MIT',
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    description='Beaker session interface for Flask.',
    long_description=open('README.rst').read(),
    py_modules=['flask_beaker'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Beaker'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    #test_suite='test_bcrypt'
)
