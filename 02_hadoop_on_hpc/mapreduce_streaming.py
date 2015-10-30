#!/usr/bin/python
#
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Template for python Hadoop streaming.  Fill in the map() and reduce()
# functions, which should call emit(), as appropriate.
#
# Test your script with
#  cat input | python map_reduce.py map | sort | python wordcount.py reduce

import sys
import re
try:
    import simplejson as json
except ImportError:
    import json

import __builtin__

def map(line):
    try:
        words = line.split()
        http_response_code = words[-2]
        emit(http_response_code, str(1))
    except:
        pass
    
def reduce(key, values):
    emit(key, str(sum(__builtin__.map(int,values))))

# Common library code follows:

def emit(key, value):
    """
    Emits a key->value pair.  Key and value should be strings.
    """
    try:
        print "\t".join( (key, value) )
    except:
        pass

def run_map():
    """Calls map() for each input value."""
    for line in sys.stdin:
        line = line.rstrip()
        map(line)

def run_reduce():
    """Gathers reduce() data in memory, and calls reduce()."""
    prev_key = None
    values = []
    for line in sys.stdin:
        line = line.rstrip()
        key, value = re.split("\t", line, 1)
        if prev_key == key:
            values.append(value)
        else:
            if prev_key is not None:
                reduce(prev_key, values)
            prev_key = key
            values = [ value ]

    if prev_key is not None:
        reduce(prev_key, values)

def main():
    """Runs map or reduce code, per arguments."""
    if len(sys.argv) != 2 or sys.argv[1] not in ("map", "reduce"):
        print "Usage: %s <map|reduce>" % sys.argv[0]
        sys.exit(1)
    if sys.argv[1] == "map":
        run_map()
    elif sys.argv[1] == "reduce":
        run_reduce()
    else:
        assert False

if __name__ == "__main__":
  main()
