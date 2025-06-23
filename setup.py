from setuptools import setup, find_packages

setup(
    name='chumdump',
    version='0.1.0',
    description='A privacy-first CLI to poison behavioral data trails before deletion.',
    author='Melisa K. Savich',
    author_email='your.email@example.com',
    url='https://github.com/YOUR_USERNAME/chumdump',
    packages=find_packages(include=['modules', 'modules.*']),
    py_modules=['chumdump'],
    install_requires=[
        'click>=8.1,<9.0'
    ],
    entry_points={
        'console_scripts': [
            'chumdump=chumdump:chumdump'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Security',
        'Topic :: Utilities'
    ],
    python_requires='>=3.7',
)
