import subprocess
import sys
# from util import log

cmd = 'g++ '
src = ['src/*.cpp']
include = ['-Iincludes']
link = []
output = 'Gutenburg.out'


if len(sys.argv) > 1:
    if sys.argv[1] == 'install':
        # subprocess.run("sudo yum install -y g++", shell=True)
        # subprocess.run("sudo yum install -y freeglut freeglut-devel glew glew-devel", shell=True)
        # subprocess.run("sudo yum install -y glm-devel", shell=True)

        subprocess.run('sudo yum install -y SDL2 SDL2-devel SDL2_image SDL2_image-devel SDL2_ttf SDL2_ttf-devel', shell=True)


    
    if sys.argv[1] == 'm':
        cmd = cmd + ' '.join([x for x in src]) + ' ' +\
            ' '.join([x for x in include]) + ' ' + \
            ' '.join([x for x in link]) + ' ' +\
            '-o ' + output

        subprocess.run(cmd, shell=True)

    if sys.argv[1] == 'r':
        subprocess.run('python ./script/main.py', shell=True)

    # if sys.argv[1] == 'c':
    #     subprocess.run('python util/clean.py .out safety=false', shell=True)
    #     subprocess.run('python util/clean.py .pyc safety=false', shell=True)
    #     subprocess.run('rmdir ./util/__pycache__', shell=True)

    # if sys.argv[1] == 'pull':
    #     subprocess.run("git pull", shell=True)

    # if len(sys.argv) > 2:
    #     if sys.argv[1] == 'push':
    #         log.log(sys.argv[2], 'changelog')
    #         subprocess.run('python util/clean.py .out safety=false', shell=True)
    #         subprocess.run('python util/clean.py .pyc safety=false', shell=True)
    #         subprocess.run('rmdir ./util/__pycache__', shell=True)
    #         subprocess.run("git add .", shell=True)
    #         subprocess.run("git commit -m '{0}'".format(sys.argv[2]), shell=True)
    #         subprocess.run("git push", shell=True)

# else:
#     cmd = cmd + ' '.join([x for x in src]) + ' ' +\
#             ' '.join([x for x in include]) + ' ' + \
#             ' '.join([x for x in link]) + ' ' +\
#             '-o ' + output

#     subprocess.run(cmd, shell=True)
#     subprocess.run('./' + output, shell=True)