#! /usr/bin/env python

import os, sys
import pickle


if __name__ == "__main__":  
    
    if len(sys.argv)!=2:
        print "Usage: " + sys.argv[0] + " <pickle file to execute>"
        sys.exit(1)
    
    pcu_file = sys.argv[1]
    #print "Read: %s"%pcu_file
    with open(pcu_file, "r") as f:
        pcu_cp = f.read()
    
    
    pcu_from_cp = pickle.loads(pcu_cp)
    result = pcu_from_cp.execute()

    print str(result.tolist())