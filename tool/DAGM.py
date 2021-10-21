import os
import sys
import shutil

def GetAllDefectiveSamplesInDAGM(path):
    classes = ['Class' + str(i+1) for i in range(10)]
    subDirs = ['Train', 'Test']
    for cls in classes:
        newPath = os.path.join(path, cls+'_relabel')
        os.mkdir(newPath)
        for sd in subDirs:
            newSubDir = os.path.join(newPath, sd)
            os.mkdir(newSubDir)
            defectives = [x[:4]+x[-4:] for x in os.listdir(os.path.join(path, cls, sd, 'Label')) if x.endswith('PNG')]
            for image in defectives:
                shutil.copyfile(os.path.join(path, cls, sd, image), os.path.join(newSubDir, image))

if __name__ == '__main__':
    path = './'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    GetAllDefectiveSamplesInDAGM(path)