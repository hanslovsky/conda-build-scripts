from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='jrun-paintera-conversion-helper',
    version='0.1.1',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='paintera-conversion-helper',
    url='https://github.com/saalfeldlab/paintera-conversion-helper',
    py_modules=['paintera_conversion_helper'],
    entry_points={
        'console_scripts': [
            'paintera-conversion-helper=paintera_conversion_helper:jrun_paintera_conversion_helper'
        ]
    },
)
