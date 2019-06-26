from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='paintera-conversion-helper',
    version='0.7.0',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='paintera-conversion-helper',
    url='https://github.com/saalfeldlab/paintera-conversion-helper',
    py_modules=[
        'paintera_conversion_helper',
        'extract_to_scalar'
        ],
    entry_points={
        'console_scripts': [
            'paintera-conversion-helper=paintera_conversion_helper:jgo_paintera_conversion_helper',
            'paintera-extract-highest-resolution-as-scalar=extract_to_scalar:extract'
        ]
    },
    install_requires=['jgo', 'psutil']
)
