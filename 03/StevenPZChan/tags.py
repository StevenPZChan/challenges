import re
from collections import Counter
from difflib import SequenceMatcher
from itertools import product

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = '../rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED, 'r') as f:
        return TAG_HTML.findall(f.read().replace('-', ' ').lower(), re.S)


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    c = Counter()
    for tag in tags:
        c[tag] += 1
    sorted_tags = sorted(c.items(), key=lambda t: t[1], reverse=True)
    return sorted_tags[:TOP_NUMBER]


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""

    for t1, t2 in product(tags, repeat=2):
        if len(t1) < len(t2) and SequenceMatcher(None, t1, t2).ratio() > SIMILAR:
            yield (t1, t2)


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
