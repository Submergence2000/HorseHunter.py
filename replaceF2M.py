replaceTable = [
    ['妈', '爸'],
    ['🐴', '👴'],
    ['🐎', '👴'],
    ["母亲",  "父亲"],
    ["母",  "公"],
    ["你吗",  "你爹"],
    ["逼",  "屌"],
    ["阴道",  "肛门"],
    ["处女",  "处男"],
    ["娘", "爹"],
    ["她",  "他"],
]


def replaceF2M(s):
    r = s
    for replace in replaceTable:
        r = r.replace(*replace)
    return r
