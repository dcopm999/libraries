import os
from setuptools import setup


from distutils.core import Extension, setup
# from Cython.Build import cythonize, build_ext

# define an extension that will be cythonized and compiled

'''
extensions = [
        Extension(name="api", sources=["libraries/api.py"]),
        Extension(name="auth", sources=["libraries/auth.py"]),
        Extension(name="base", sources=["libraries/base.py"]),
]
'''

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

    os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

    setup(
        name='libraries',
        version='0.1.1',
        packages=['libraries'],
        include_package_data=True,
        license='BSD License',
        description='Набор стандартных библиотек',
        long_description=README,
        url='http://crm.atm.uz/',
        author='Pavel Tanchev',
        author_email='dcopm999@gmail.com',
        install_requires=[
            "aiohttp>=3.5.4",
            "Django>=2.2.5",
        ],
        # ext_modules=cythonize(extensions),
        # cmdclass={'build_ext': build_ext},
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
