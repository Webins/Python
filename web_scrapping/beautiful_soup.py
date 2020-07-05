from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")

# body
print(soup.body)
# head
print(soup.head)
# find the first div
print(soup.find("div"))
# find all the li (return a list)
print(soup.find_all("li"))
# find by id
print(soup.find(id="first"))
# find by class
print(soup.find_all(class_="special"))
# find by attribute
print(soup.find_all(attrs={"data-example": "yes"}))
# css selectos
print(soup.select("#first"))
print(soup.select(".special"))
print(soup.select("[data-example]"))
# select allways return a list
# soup return an object not a string
print(type(soup))
print(type(soup.head))


# extract data from elements
elements = soup.select(".special")
for element in elements:
  # get the name of the element
  print(element.name)
  # get the text
  print(element.get_text())
  # get the attributes
  print(element.attrs)


# navigating with beautiful soup
# give me everything inside body returns a list()
data = soup.body.contents
print(data)
# give me the first element that appears in body
print(data[1])
# give me the next sibling
print(data[1].next_sibling.next_sibling)
print(data[1].find_next_sibling())
# i can loop for every sibling in the body
for siblings in data:
  if siblings == '\n': continue
  else: print(siblings)

# give me the parent of data [1]
print(data[1].parent)