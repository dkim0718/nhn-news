This is a simple python script to copy news articles from NHN.

How to use:
1. Search for your desired news article on newslibrary
2. Click article
3. Press Command + Option + I to open developer tools
4. Press Command + R to reload the article
5. Close the mouse usage notification (if open)
6. Type 'json' in top left 'Filter' box (below the red dot)
7. Right click on the bottom-most item on the Name list
8. Click on Copy -> Copy Response
9. Open 'article.txt' and delete contents
10. Paste the response you copied into article.txt and save
11. Open a terminal window and type python download_article.py
12. Done!
