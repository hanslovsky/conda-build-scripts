from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='jrun-paintera',
    version='0.1.0',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='paintera',
    url='https://github.com/saalfeldlab/paintera',
    py_modules=['paintera'],
    entry_points={
        'console_scripts': [
            'paintera=paintera:jrun_paintera'
        ]
    },
)
