replaceTable = [
    ['妈', '爸'],
    ['🐴', '爹'],
    ['🐎', '爹'],
    ["妈",  "爸"],
    ["🐴",  "爹"],
    ["🐎",  "爹"],
    ["母亲",  "爹"],
    ["母",  "公"],
    ["你吗",  "你爹"],
    ["逼",  "屌"],
    ["阴道",  "肛门"],
    ["处女",  "处男"],
    ["她",  "他"],
]


def replaceF2M(s):
    r = s
    for replace in replaceTable:
        r = r.replace(*replace)
    return r
