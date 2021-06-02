import os
import re
from func import get_movie_db, close_array, get_response


file_name = 'output/bayDB.json'  # output file name
main_url = 'https://www.imdb.com/name/nm0000881/?ref_=nv_sr_srsg_0'  # Director URL
main_response = get_response(main_url)  # Getting response for Director URL

pattern = re.compile(r'(<b>)(.*)(\s)(.*?)(</b>)')  # Forming Pattern object
entries = pattern.finditer(main_response.text)  # Extracting elements satisfying pattern

movie_dict = {}  # Empty Director will be having {'MovieName' : 'Movie IMDB Link'}
for text in entries:
    name = text.group(4).split('>')[1].split('<')[0]
    link = 'https://www.imdb.com' + text.group(2).split('"')[1]
    movie_dict[name] = link
print(movie_dict)

try:
    os.remove(file_name)  # Removing Output File if already exists
    print('File successfully deleted !!')
except FileNotFoundError as e:
    print('No File Found !')

try:
    get_movie_db(movie_dict.values(), file_name)  # Preparing Movie Database
except Exception as e:
    raise e
finally:
    close_array(file_name)  # Closing Json Array













