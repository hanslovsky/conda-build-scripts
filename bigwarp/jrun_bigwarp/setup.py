from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='bigwarp',
    version='3.1.2dev',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='bigwarp',
    url='https://github.com/saalfeldlab/bigwarp',
    py_modules=['jrun_bigwarp'],
    entry_points={
        'console_scripts': [
            'bigwarp=jrun_bigwarp:bigwarp'
        ]
    },
)
