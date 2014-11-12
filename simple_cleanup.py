#!/usr/bin/env python
import subprocess as sp
import re
import argparse

# #######################
# Python replacement
# #######################
# Replacements that can be made with string.replace()
repl_tuple_list = [('\t', '    '), 
                   ('( ', '('),
                   (' )', ')'),
                   ('[ ', '['),
                   (' ]', ']')]

# ####################################
# Replace a single file's contents
# ####################################
def replace(input_contents):

    # Make replacements
    output_contents = input_contents
    for repl_tuple in repl_tuple_list:
        output_contents = output_contents.replace(*repl_tuple)

    return output_contents

# ########################################
# Wrapper for each individual input file
# ########################################
def file_wrapper(input_file, args):

    # Open input file, read contents
    with open(input_file, 'r') as inp:
        input_contents = inp.read()

    # Save as backup file
    backup_file = input_file + args.backup_ext
    with open(backup_file, 'w') as bak:
        bak.write(input_contents)

    ### Edit file contents, overwrite input file
    output_contents = replace(input_contents)
    with open(input_file, 'w') as outp:
        outp.write(output_contents)

# ##################################

# ##################################
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--backup-ext', default='.BAK', metavar='BAK', help="Edit files in-place, using %(metavar)s as backup extension.")
    parser.add_argument('files', metavar='file', nargs='+', help='File to edit.')  # Will always return a list
    args = parser.parse_args()
    
    assert len(args.backup_ext) > 0
    assert isinstance(args.files, list)

    # Call file_wrapper() on each input file
    for input_file in args.files:
        file_wrapper(input_file, args)

