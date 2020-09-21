from os import path

from setuptools import setup, find_packages

# setup metainfo
libinfo_py = path.join('bert_serving', 'server', '__init__.py')
libinfo_content = open(libinfo_py, 'r').readlines()
version_line = [l.strip() for l in libinfo_content if l.startswith('__version__')][0]
exec(version_line)  # produce __version__

setup(
    name='albert_serving_server',
    version=__version__,
    description='Mapping a variable-length sentence to a fixed-length vector using BERT model (Server)',
    url='https://github.com/maomao905/albert-as-service',
    long_description=open('README.md', 'r', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    author='Han Xiao',
    author_email='artex.xh@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'numpy',
        'six==1.15.0',
        'pyzmq>=17.1.0',
        'GPUtil>=1.3.0',
        'termcolor>=1.1',
        'sentencepiece',
    ],
    extras_require={
        'cpu': ['tensorflow>=1.15.2'],
        'gpu': ['tensorflow-gpu>=1.15.2'],
        'http': ['flask', 'flask-compress', 'flask-cors', 'flask-json', 'bert-serving-client', 'flasgger']
    },
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ),
    entry_points={
        'console_scripts': ['albert-serving-start=bert_serving.server.cli:main',
                            'albert-serving-benchmark=bert_serving.server.cli:benchmark',
                            'albert-serving-terminate=bert_serving.server.cli:terminate'],
    },
    keywords='bert nlp tensorflow machine learning sentence encoding embedding serving',
)
