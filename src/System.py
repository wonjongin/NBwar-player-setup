import platform


def check_os():
    res = platform.system()
    if res == 'Darwin':
        res = 'macOS'
    return res
