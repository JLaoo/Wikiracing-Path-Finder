Link to original repository: https://github.com/JLaoo/Wikiracing-Path-Finder
# Wikiracing Path Finder
Wikiracing (also known as The Wikipedia Game, Wikipedia Maze, etc.) is a game where players start from a page on Wikipedia and try to reach a destination page in either the quickest amount of time or the lowest number of clicks ([Wikipedia](https://en.wikipedia.org/wiki/Wikiracing)). This is a script that attempts to find a path that requires the least amount of clicks using Scrapy.
# Methodology
This script simply takes all links on a wikipedia page that lead to other wikipedia pages from top to bottom. I intended for it to be a Breadth-First search but I think the script actually probably only scrapes the URLs near the top of the page as it searches for a path due to the limit of concurrent crawls I gave it. The code will probably require some serious reworking to use an actual Breadth-First search algorithm.
# Notes
- The game pulls its start and end destinations from [here](https://www.thewikigame.com/group). In order to get the pages, I had to pull a sneaky and find the [API](https://api.thewikigame.com/api/v1/group/22033570-e1fd-4a9f-9a96-9068082b88aa/current-round/) which could be changed in the future. The API also requires an aurhotrization token to retrieve info from which may also be changed in the future, but it shouldn't be hard to find via inspection through a browser. You can also easily just manually put in start and end pages in the spider itself.
- The spider simply returns the first path to the destination it finds which may not actually be the shortest path since I didn't want the spider to keep running and digging for a shorter path, but the found path will be relatively short.
- The settings can be messed around with and proxies can be used in order to speed up the script, but I enabled throttling and obeying robots.txt for the sake of complying with TOS.
- The path is returned in a .txt file in the spiders folder. An example path has been provided.

# To Do
- Rework into proper Breadth-First search algorithm.
- Pull info from MediaWiki API instead of parsing entire Wikipedia pages with BeautifulSoup.
- Fix encoding of path in .txt output.

# Disclaimer
- I do not endorse the use of this spider to cheat at the wikigame. The usage of this spider is at the discretion of the user.
