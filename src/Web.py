import requests


def webFileSize(url):
    r = requests.head(url)
    file_size = int(r.headers.get('content-length', 0))
    print(f'Size of file: {file_size}')
    return file_size


def webFileDownload(url, path):
    fileName = path.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(32 * 1024):
            f.write(chunk)


def webFileDownloadwithPbar(url, path, pbar):
    fileName = path.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(32 * 1024):
            f.write(chunk)
            pbar.setValue(len(chunk))
