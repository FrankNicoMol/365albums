def capitalize(string):
    return string[0].upper() + string[1:]


def load_urls(links_path):
    with open(links_path, 'r') as f:
        text = f.read()
    return text.strip().split()


def write_to_markdown(albums, path):
    markdown_entries = [f'{i + 1:03d}. [{album[0][0]} - {album[0][1]}]({album[1]})' for i, album in enumerate(albums)]
    with open(path, 'w') as f:
        f.write('\n'.join(markdown_entries))


def load_markdown_albums(markdown_path):
    with open(markdown_path, 'r') as f:
        text = f.read()

    list_albums = []
    for line in text.split('\n'):
        if line:
            album_name = line.split(' - ')[1].split(']')[0]
            artist_name = line.split(' - ')[0].split('[')[1]
            url_link = line.rsplit('(', 1)[1].rsplit(')', 1)[0]
            list_albums.append([[artist_name, album_name], url_link])

    return list_albums
