Link to original repository: https://github.com/JLaoo/Wikiracing-Path-Finder
# Wikiracing Path Finder
Wikiracing (also known as The Wikipedia Game, Wikipedia Maze, etc.) is a game where players start from a page on Wikipedia and try to reach a destination page in either the quickest amount of time or the lowest number of clicks([Wikipedia Article](https://en.wikipedia.org/wiki/Wikiracing)). This is a script that attempts to find a path that requires the least amount of clicks with scrapy.
# Notes
- The game pulls its start and end destinations from [here](https://www.thewikigame.com/group). In order to get the pages, I had to pull a sneaky and find the [API](https://api.thewikigame.com/api/v1/group/22033570-e1fd-4a9f-9a96-9068082b88aa/current-round/) which could be changed in the future. The API also requires an aurhotrization token to retrieve info from which may also be changed in the future, but it shouldn't be hard to find via inspection through a browser. You can also easily just manually put in start and end pages in the spider itself.
- The spider simply returns the first path to the destination it finds which may not actually be the shortest path since I didn't want the spider to keep running and digging for a shorter path, but the found path will be relatively short.
- The settings can be messed around with and proxies can be used in order to speed up the speed up the script, but I enabled throttling and obeying robots.txt for the sake of complying with TOS.
- The path is returned in a .txt file in the spiders folder. An example path has been provided.
