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
    argv               = repository_strings + endpoint + sys.argv[1:]

    jrun.jrun.jrun_main(argv)
    

