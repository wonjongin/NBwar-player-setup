import os
import zipfile
import shutil
import platform


def getMinecraftDir():
    system = platform.system()
    homePath = os.path.expanduser('~')
    res = ''
    if system == 'Windows':
        res = '%APPDATA%/.minecraft'
    elif system == 'Darwin':
        res = homePath + '/Library/Application Support/minecraft'
    elif system == 'Linux':
        res = homePath + '/.minecraft'
    else:
        res = ''
    return res


def createDir(dirPath):
    try:
        if not(os.path.isdir(dirPath)):
            os.makedirs(os.path.join(dirPath))
    except OSError as e:
        if e.errno != e.errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise


def unzip(path):
    fileName = path.split('/')[-1]
    dirName = fileName.replace('.zip', '')
    createDir(path.replace('.zip', ''))
    zipfile.ZipFile(path).extractall(path.replace('.zip', ''))


def rmr(path):
    shutil.rmtree(path)


def rmrmods():
    dirPath = getMinecraftDir()+"/mods"
    rmr(dirPath)
