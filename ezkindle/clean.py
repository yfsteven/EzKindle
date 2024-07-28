import re
from collections import Counter

def remove_dups(l):
    counts = Counter(l)

    return [item for item, count in counts.items() if count == 1]

def cleanse(clip):

    jp_added_regex = r'^- 位置No.+'

    with open(clip, 'r', encoding='utf-8-sig') as f:
        clipping = f.readlines()

        sanitised = [re.sub(jp_added_regex, '', line) for line in clipping]

        marble = remove_dups(sanitised)

    return marble





