import os
import re
import zipfile
import string
from progress import ProgressTracker

import sys

def cleanup(str): return ''.join([s for s in str.lower() if s in string.ascii_lowercase])

def get_all_items_cwd(recursive = True):
    return get_items_cwd(regex=False, recursive=recursive)

def get_items_cwd(item='', regex=True, recursive=True, BASE_DIR = os.getcwd()):
    dir = []
    for items in os.listdir():
        if os.path.isdir(items):
            if recursive:
                os.chdir(os.getcwd() + '/' + items)
                dir += get_items_cwd(item=item, regex=regex, recursive=recursive, BASE_DIR=BASE_DIR)          
              
        else:
            file = os.getcwd() + '/' + items
            if regex:
                if re.search(item, file) is not None: dir.append(file)
            else: 
                if re.search(item + '$', file) is not None: dir.append(file)

    if BASE_DIR == os.getcwd():
        return dir
    else:
        os.chdir('..')
        return dir

def extract_items(dir = os.getcwd(), target_dir=''):
    os.chdir(dir)
    files = get_items_cwd(item='.zip', regex=False, recursive=True)
    
    tracker = ProgressTracker(files, 'Extracting...')
    for file in files:
        tracker.update()
        newdir = file.split('/')
        newdir = target_dir + newdir[-1].replace('.zip', '')
        if not os.path.isdir(newdir): os.mkdir(newdir)
        try:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(newdir)
        except:
            pass

def clean_items(dir = os.getcwd(), target_dir = ''):
    os.chdir(dir)
    files = get_items_cwd(item='.txt', regex=False, recursive=True)
    
    tracker = ProgressTracker(files, 'Cleaning...')
    for file in files:
        tracker.update()
        try:
            with open(file, 'r') as txt_file:
                with open(target_dir+'/master.txt', 'a') as master:
                    for line in txt_file.readlines():
                        clean = cleanup(line)
                        master.write(clean)

        except:
            pass
        os.remove(file)



