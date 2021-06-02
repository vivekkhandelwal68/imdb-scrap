import requests
import re
import json


def get_list(matches, groupnum):
    lst = []
    for match in matches:
        lst.append(match.group(groupnum))
    return lst


def get_response(url):
    res = requests.get(url)
    return res


def write_file(file, desc):
    content = json.loads(desc)
    with open(file, 'a') as f:
        if f.tell() != 0:
            f.write(',\n')
        else:
            f.write('[\n')
        json.dump(content, f, indent=2)


def close_array(file):
    with open(file, 'a') as f:
        f.write('\n]')


def get_movie_db(url_list, file_name):
    for url in url_list:
        response = get_response(url)
        moviedescpattern = re.compile(r'("application/ld\+json">)(.*?)(</script>)')
        moviedescmatches = moviedescpattern.finditer(response.text)
        moviedesc = get_list(moviedescmatches, 2)
        write_file(file_name, moviedesc[0]) if len(moviedesc) > 0 else print(f'no item found for {url}')
