from distutils.core import USAGE
import sys, os

from interface import DBDB

def main(argv):
    if not (4 <= len(argv) <= 5):
        USAGE()
        return 'BAD_ARGS'
    
    dbname, verb, key, value = (argv[1:] + [None])[:4]
    if verb not in {'get', 'set', 'delete'}:
        USAGE()
        return 'BAD_VERB'
    
    db = DBDB.connect(dbname)          
    
    try:
        if verb == 'get':
            sys.stdout.write(db[key])  
        elif verb == 'set':
            db[key] = value
            db.commit()
        else:
            del db[key]
            db.commit()
    except KeyError:
        print("Key not found", file=sys.stderr)
        return 'BAD_KEY'
    return 'OK'