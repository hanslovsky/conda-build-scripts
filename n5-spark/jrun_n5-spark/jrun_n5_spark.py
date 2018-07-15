import jrun.jrun
import os
import psutil
import sys

repositories = {
    'saalfeldlab'   : 'https://saalfeldlab.github.io/maven',
    'imagej.public' : 'https://maven.imagej.net/content/groups/public'
    }

def add_jvm_args_as_necessary(argv):
    gc_option = '-XX:+UseConcMarkSweepGC'

    if not gc_option in argv:
        argv += [gc_option]

    for arg in argv:
        if '-Xmx' in arg:
            return argv

    total_memory  = psutil.virtual_memory().total
    exponent      = 3 if total_memory > 2*1024**3 else 2
    memory_unit   = 'G' if exponent == 3 else 'M'
    max_heap_size = os.getenv(
        'N5_SPARK_MAX_HEAP_SIZE',
        '{}{}'.format(max(total_memory // (1024**exponent) // 2, 1), memory_unit))

    spark_master  = os.getenv('SPARK_MASTER', 'local[*]')
    argv = ['-Xmx{}'.format(max_heap_size)] + ['-Dspark.master={}'.format(spark_master)] + argv

    return argv

def n5_convert():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.N5ConvertSpark')

def n5_downsample_label():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.N5LabelDownsamplerSpark')

def n5_downsample_offset():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.N5OffsetDownsamplerSpark')

def n5_downsample():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.N5DownsamplerSpark')

def n5_mips():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.N5MaxIntensityProjection')

def n5_remove():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.N5RemoveSpark')

def n5_scale_pyramid_nonisotropic_3d():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.scalepyramid.N5NonIsotropicScalePyramidSpark3D')

def n5_scale_pyramid_offset():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.scalepyramid.N5OffsetScalePyramidSpark')

def n5_scale_pyramid():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.downsample.scalepyramid.N5ScalePyramidSpark')

def n5_slice_tiff():
    n5_spark_base('org.janelia.saalfeldlab.n5.spark.N5SliceTiffConverter')

def n5_spark_base(main_class):
    argv               = sys.argv[1:]
    double_dash_index  = [i for (i, arg) in enumerate(argv) if arg == '--'][0] if '--' in argv else -1
    jrun_and_jvm_argv  = ([] if double_dash_index < 0 else argv[:double_dash_index]) + ['--ignore-jrunrc']
    repository_strings = ['-r'] + ['{}={}'.format(k, v) for (k, v) in repositories.items()]
    endpoint           = ['org.janelia.saalfeldlab:n5-spark:{}'.format(main_class)] if os.getenv('SPARK_PROVIDED', None) else ['org.janelia.saalfeldlab:n5-spark:{}+org.apache.spark:spark-core_2.11:2.2.0'.format(main_class)]
    n5_argv            = argv if double_dash_index < 0 else argv[double_dash_index+1:]
    argv               = add_jvm_args_as_necessary(jrun_and_jvm_argv) + repository_strings + endpoint + n5_argv

    jrun.jrun.jrun_main(argv)

