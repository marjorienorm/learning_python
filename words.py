"""Retrieve and print words for a url.

usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words form a url.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.

    """
    story = urlopen(url)

    story_words = []
    for line in story:
        #line_words = line.split()
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append( word )
    
    story.close()

    return story_words


def print_items( items ):    
    """Print items oer line from a list of items.

    Args:
        items: An iterable series of printable items.

    Returns:
        Nothing is returned from this function.
    """
    for item in items:
        print( item )


def main(url = None):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        Nothing is returned from this function.
    """

    if url is None:
        url = "http://sixty-north.com/c/t.txt"

    words = fetch_words(url)
    print_items( words )


#def main():
#    words = fetch_words( "http://sixty-north.com/c/t.txt" )
#    print_items( words )


if __name__ == '__main__':    
    if len(sys.argv) > 1:
       main( sys.argv[1] )
    else:
        main()