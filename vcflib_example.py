#!/usr/bin/env python

import sys
import time
from itertools import islice
from vcflib import PyVariantCallFile


if __name__ == '__main__':
    filename = sys.argv[1]
    print 'parsing %s ...' % filename

    vcf = PyVariantCallFile(filename)
    print 'INFO fields: %s' % vcf.infoIds
    print 'FORMAT fields: %s' % vcf.formatIds
    print 'FILTER fields: %s' % vcf.filterIds
    print 'samples: %s' % vcf.sampleNames
    before = time.time()
    n = len(vcf)
    after = time.time()
    print 'found %s variants in %ss' % (n, after-before)

    vcf = PyVariantCallFile(filename)
    vcf.parseSamples = False
    before = time.time()
    n = len(vcf)
    after = time.time()
    print 'found %s variants in %ss (without parsing samples)' % (n, after-before)

    vcf = PyVariantCallFile(filename)
    print 'first 3 variants...'
    for v in islice(vcf, 3):
        print v
    

