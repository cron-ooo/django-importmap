import setuptools

setuptools.setup(
    name='django-importmap',
    version='0.1',
    description='A Django app to dynamically import',
    url='https://github.com/cron-ooo/django-importmap',
    author='Akhmed Gaziev',
    author_email='mail@akhmedgaziev.ru',
    license='BSD',
    packages=setuptools.find_packages(),
    install_requires=[
        'django',
        'requests',
    ],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
