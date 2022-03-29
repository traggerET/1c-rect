def kmp_search(pat, txt):
    pattern_len = len(pat)
    source_len = len(txt)

    prefixes = [0] * pattern_len
    j = 0

    prefix(pat, prefixes)
    occurences = set()
    i = 0
    while i < source_len:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == pattern_len:
            occurences.add(i - j)
            j = prefixes[j - 1]

        elif i < source_len and pat[j] != txt[i]:
            if j != 0:
                j = prefixes[j - 1]
            else:
                i += 1
    return occurences


# counting longest prefix
def prefix(pat, prefixes):
    len_ = 0
    i = 1

    while i < len(pat):
        if pat[i] == pat[len_]:
            len_ += 1
            prefixes[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = prefixes[len_ - 1]
            else:
                prefixes[i] = 0
                i += 1
