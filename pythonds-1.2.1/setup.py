from setuptools import setup, find_packages
setup(
    name = "pythonds",
    description = 'Data structures package for Problem Solving with Algorithms and Data Structures using Python',
    author = 'Brad Miller',
    author_email = 'bonelake@mac.com',
    license = 'GPL',
    keywords = ['Education', 'Data Structures', 'Stack', 'Queue', 'Tree', 'Graph'],
    version = "1.2.1",
    url = 'https://github.com/bnmnetp/pythonds',
    packages = find_packages(),
    classifiers=('Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Education',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Operating System :: MacOS',
                   'Operating System :: Unix',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Education'),
    long_description=open('README.rst').read()
)
