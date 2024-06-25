# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
#
# # Write your code below this line 👇
#
#
# resp = requests.get(URL)
# resp.raise_for_status()
# soup = BeautifulSoup(resp.text, "html.parser")
#
#
# titles = [title.getText() + '\n' for title in soup.find_all('h3', class_='title')[::-1]]
#
# with open("./movies.txt", 'w') as file:
#     contents = file.writelines(titles)