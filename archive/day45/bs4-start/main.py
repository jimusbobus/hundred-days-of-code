from bs4 import BeautifulSoup
import requests

resp = requests.get("https://news.ycombinator.com/")
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

# print(soup.select(selector="span.titleline a")[1].text)

# top_story = soup.find_all('span', class_='titleline')[0]

stories = []

for story in soup.find_all('span', class_='titleline'):
    # print(story)
    stories.append({
        'name': story.a.text,
        'href': story.a.get("href")
    })

# print(stories[0])

story_points = [int(story.getText().split()[0]) for story in soup.find_all('span', class_='score')]

highest_int = max(story_points)
highest_int_index = story_points.index(highest_int)
print(highest_int)
print(stories[highest_int_index])


# with open("./website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.find_all(name="li"))
#
# val = [tag.get("href") for tag in soup.find_all(name="a")]
#
# print(val)
#
# print(soup.select(".heading"))

