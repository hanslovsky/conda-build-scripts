from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='jrun-bigcat',
    version='0.0.3-beta-1',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='bigcat',
    url='https://github.com/saalfeldlab/bigcat',
    py_modules=['jrun_bigcat'],
    entry_points={
        'console_scripts': [
            'bigcat=jrun_bigcat:jrun_bigcat'
        ]
    },
)
