#!/usr/bin/python3

import os
import unicodedata

# this script walkt through all the files in this directory down to the bottom one and replaces some 
# part of the filename and pathname

#flags:

simulate = True
files_only =  False
go_down = True
lowercase = True
replace_sets = (('_', ("%20",)),
				('_', set(" []}{()+!,;:")),
	            ("-", set("~")),
	            ("",  set("!@#$%^*=\'\"\\/<>")),
	            ("_and_", ("&",))
	           )


currentdir  = os.curdir
print(currentdir)

def replace_chars(filename, replace_sets = replace_sets, lowercase = True, remove_duplicate = True, remove_accent = True):
	
	for n, lst in replace_sets:
		for l in lst:
			filename = filename.replace(l, n)

	if lowercase:
		filename = filename.lower()

	if remove_accent:
		filename = remove_accent_characters(filename)

	if remove_duplicate:
		filename = '_'.join(f for f in filename.split('_') if f != '')
		filename = '-'.join(f for f in filename.split('-') if f != '')
	return filename

def remove_accent_characters(textblock):
    nfkd_form = unicodedata.normalize('NFKD', textblock)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def is_valid_replace(filename, other_files, root):
	if filename in other_files:
		print('error, {} is dublicate in folder {}'.format(filename, root))
		return False
	return True
 

def rename_files_and_dirs(path, replace_sets = replace_sets, lowercase = True, remove_duplicate = True, simulate = True ):

	for root, dirs, files in os.walk(path):
#		print('working on', root)
		for file in files:
			newfile = replace_chars(file, replace_sets, lowercase, remove_duplicate)
			if not simulate and newfile != file and is_valid_replace(newfile, files, root):
				os.rename(os.path.join(root, file), os.path.join(root, newfile))
				print(root, file, '===>', newfile)

		for i, d in enumerate(dirs):
			newdir = replace_chars(d, replace_sets, lowercase, remove_duplicate)
			if not simulate and newdir != d and is_valid_replace(newdir, dirs, root):
				dirs[i] = newfile
				os.rename(os.path.join(root, d), os.path.join(root, newdir))
				print(root, d, '===>', newdir)

if __name__ == "__main__":
	rename_files_and_dirs(currentdir, lowercase = False, remove_duplicate = True, simulate = False)
