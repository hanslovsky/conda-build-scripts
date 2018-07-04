import jrun.jrun
import os
import sys

repositories = {
    'saalfeldlab'   : 'https://saalfeldlab.github.io/maven',
    'imagej.public' : 'https://maven.imagej.net/content/groups/public'
    }

def jrun_paintera_conversion_helper():
    repository_strings = ['-r'] + ['{}={}'.format(k, v) for (k, v) in repositories.items()]
    endpoint           = ['org.janelia.saalfeldlab:paintera-conversion-helper:0.1.0']
    spark_master       = ['-D{}'.format(os.getenv('SPARK_MASTER', 'spark.master=local[*]'))]
    argv               = repository_strings + spark_master + endpoint + sys.argv[1:]


    jrun.jrun.jrun_main(argv)
    
