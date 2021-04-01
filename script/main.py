import subprocess
import batch
import os
import time
import locale
from multiprocessing import Process, Manager

import gram
import progress


def compile():
    cmd = 'g++ '
    src = ['src/*.cpp']
    include = ['-Iincludes']
    link = []
    output = 'Gutenburg.out'

    cmd = cmd + ' '.join([x for x in src]) + ' ' +\
                ' '.join([x for x in include]) + ' ' + \
                ' '.join([x for x in link]) + ' ' +\
                '-o ' + output

    subprocess.run(cmd, shell=True)
    return output

def execute(exe, process_num, batchsize, filename):
    subprocess.run(['./{0}'.format(exe), str(process_num), str(batchsize), str(filename)])

def extract(dir, rawdir):
    extractdir = dir + '/extracted/'
    if not os.path.isdir(extractdir): os.mkdir(extractdir)
    batch.extract_items(rawdir, extractdir)
    return extractdir

    
def clean(dir, extractdir):
    cleandir = dir + '/cleaned/'
    if not os.path.isdir(cleandir): os.mkdir(cleandir)
    batch.clean_items(extractdir, cleandir)
    subprocess.run(['rm -r {0}'.format(extractdir)], shell=True)
    return cleandir

def process(exe, dir, cleandir):
    os.chdir(dir)

    gramdir = dir + '/grams/'
    if not os.path.isdir(gramdir): os.mkdir(gramdir)

    workers = 8

    masterpath = cleandir + 'master.txt'

    filesize = os.path.getsize(masterpath)
    batchsize = filesize / workers

    manager = Manager()
    processes = manager.list([])

    locale.setlocale(locale.LC_ALL, 'en_US')


    ## Process header ##
    print("\n>> Processing Dataset: Filesize {0} bytes,  Workers: "\
              .format(locale.format_string("%d", filesize, grouping=True)), workers)

    print("=" * 70)

    ps = []
    for i in range(workers):
        p = Process(target=execute, args=[exe, i, batchsize, masterpath])
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    print("\033[{0};0H".format(workers + 4))
    print("Workers finished processing...")
    subprocess.run(['rm -r {0}'.format(cleandir)], shell=True)
    subprocess.run(['rm {0}'.format(exe)], shell=True)

    return gramdir

def analyze(dir, gramdir):
    masterdir = dir + '/master/'
    if not os.path.isdir(masterdir): os.mkdir(masterdir)
    print("Analyzing grams...")
    gram.run()
    print("Done")
    os.chdir(dir)
    subprocess.run(['rm -r {0}'.format(gramdir)], shell=True)
    return masterdir

def finalize(masterdir):
    print('Finalizing...')
    gram.generate_gram_list(masterdir)
    subprocess.run(['rm -r {0}'.format('./script/__pycache__')], shell=True)
    subprocess.run(['pluma {0}all_data.txt'.format(masterdir)], shell=True)


def main():
    progress.clear_screen()
    print("Frequency Analysis for English Language")
    print("=" * 70)

    basedir = os.getcwd()
    rawdir = '/home/student/Desktop/gutenburg'

    extractdir = extract(basedir, rawdir)

    cleandir = clean(basedir, extractdir)

    gramdir = process(compile(), basedir, cleandir)

    masterdir = analyze(basedir, gramdir)

    finalize(masterdir)

if __name__ == '__main__':
    main()