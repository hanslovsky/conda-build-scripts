from distutils.core import setup
from distutils.command.build_py import build_py

setup(
    name='jrun-n5-spark',
    version='3.0.0',
    author='Philipp Hanslovsky',
    author_email='hanslovskyp@janelia.hhmi.org',
    description='n5-spark',
    url='https://github.com/saalfeldlab/n5-spark',
    py_modules=['jrun_n5_spark'],
    entry_points={
        'console_scripts': [
            'n5-convert=jrun_n5_spark:n5_convert',
            'n5-downsample-label=jrun_n5_spark:n5_downsample_label',
            'n5-downsample-offset=jrun_n5_spark:n5_downsample_offset',
            'n5-downsample=jrun_n5_spark:n5_downsample',
            'n5-mips=jrun_n5_spark:n5_mips',
            'n5-remove=jrun_n5_spark:n5_remove',
            'n5-scale-pyramid-nonisotropic-3d=jrun_n5_spark:n5_scale_pyramid_nonisotropic_3d',
            'n5-scale-pyramid-offset=jrun_n5_spark:n5_scale_pyramid_offset',
            'n5-scale-pyramid=jrun_n5_spark:n5_scale_pyramid',
            'n5-slice-tiff=jrun_n5_spark:n5_slice_tiff'
        ]
    },
)
