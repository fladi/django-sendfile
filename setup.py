from distutils.core import setup
import os

# Try to import any previously install sendfile package.
# If this succeeds, check if it looks the same as this package, so we don't
# change the package name during an update.
try:
    import sendfile
except ImportError:
    package='sendfile'
    imported=False
else:
    imported=True
    if sendfile.__file__ != 'sendfile/__init__.py':
        package='django_sendfile'
    else:
        package='sendfile'
# Ensure sendfile is loaded from the 'src' path, so the version information
# can be extracted.
os.sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
if imported:
    reload(sendfile)
else:
    import sendfile


setup(
    name='django-sendfile',
    version=sendfile.__version__,
    description='Abstraction to offload file uploads to web-server (e.g. Apache with mod_xsendfile) once Django has checked permissions etc.',
    long_description=open('README.rst').read(),
    author='John Montgomery',
    author_email='john@sensibledevelopment.com',
    url='http://github.com/johnsensible/django-sendfile',
    download_url='http://github.com/johnsensible/django-sendfile/downloads',
    license='BSD',

    requires=['Django (>=1.4.2)'],

    packages=[package, '%s.backends' % package],
    package_dir={
        package: 'src/sendfile',
        '%s.backends' % package: 'src/sendfile/backends',
    },
    package_data = {
        'sendfile': ['testfile.txt'],
    },

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
