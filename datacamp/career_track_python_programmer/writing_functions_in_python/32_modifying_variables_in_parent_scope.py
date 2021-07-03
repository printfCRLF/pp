def read_files():
    file_contents = None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents = []
        with open(filename) as fin:
            file_contents.append(fin.read())

    for filename in ['data/1984.txt', 'data/MobyDick.txt', 'data/CatsEye.txt']:
        save_contents(filename)

    return file_contents


print('\n'.join(read_files()))
