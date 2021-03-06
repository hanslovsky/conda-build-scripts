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
        'BIGCAT_MAX_HEAP_SIZE',
        '{}{}'.format(max(total_memory // (1024**exponent) // 2, 1), memory_unit))

    argv = ['-Xmx{}'.format(max_heap_size)] + argv

    return argv


def jrun_bigcat():
    argv               = sys.argv[1:]
    double_dash_index  = [i for (i, arg) in enumerate(argv) if arg == '--'][0] if '--' in argv else -1
    jrun_and_jvm_argv  = ([] if double_dash_index < 0 else argv[:double_dash_index]) + ['--ignore-jrunrc']
    repository_strings = ['-r'] + ['{}={}'.format(k, v) for (k, v) in repositories.items()]
    endpoint           = ['sc.fiji:bigcat:bdv.bigcat.BigCat']
    bigcat_argv        = argv if double_dash_index < 0 else argv[double_dash_index+1:]
    argv               = add_jvm_args_as_necessary(jrun_and_jvm_argv) + repository_strings + endpoint + bigcat_argv

    jrun.jrun.jrun_main(argv)

