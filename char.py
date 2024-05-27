import chardet

def check_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    print(f"{file_path}: {result}")

check_encoding('README.md')
check_encoding('requirements.txt')
check_encoding('setup.py')