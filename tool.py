def main(argv):
    if not (4 <= len(argv) <= 5):
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (argv[1:] + [None]) [:4]
    
    if verb not in {'get', 'set', 'delete'}: #getters and setters for verb
        usage()
        return BAD_VERB 