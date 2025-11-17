import re

sample = """id\tname\tMath\tEnglish\tScience
1\tAlice\t85\t92\t88
2\tBob\t90\t88\t92
"""


def parse_text(text):
    # normalize literal \t sequences -> real tab
    text = text.replace('\\t', '\t')
    # split lines (CRLF aware)
    lines = re.split(r"\r?\n", text.strip())
    if not lines:
        return None
    first = lines[0]
    comma_count = first.count(',')
    tab_count = first.count('\t')
    delim = '\t' if (tab_count >= comma_count and tab_count > 0) else ','

    def parse_line(line, delim):
        fields = []
        cur = []
        inq = False
        i = 0
        while i < len(line):
            c = line[i]
            if c == '"':
                if inq and i+1 < len(line) and line[i+1] == '"':
                    cur.append('"')
                    i += 2
                    continue
                inq = not inq
                i += 1
                continue
            if c == delim and not inq:
                fields.append(''.join(cur).strip())
                cur = []
            else:
                cur.append(c)
            i += 1
        fields.append(''.join(cur).strip())
        return fields

    headers = parse_line(lines[0], delim)
    data = []
    for ln in lines[1:]:
        if ln.strip() == '':
            continue
        vals = parse_line(ln, delim)
        if len(vals) == 1 and delim in vals[0]:
            vals = [v.strip() for v in vals[0].split(delim)]
        obj = {}
        for i,h in enumerate(headers):
            obj[h] = vals[i] if i < len(vals) else ''
        data.append(obj)
    return headers, data, delim


def wide_to_long(data, id_vars, var_name='subject', value_name='score'):
    id_list = [v.strip() for v in id_vars.split(',')]
    cols = list(data[0].keys())
    value_cols = [c for c in cols if c not in id_list]
    out = []
    for row in data:
        for vc in value_cols:
            new = {k: row[k] for k in id_list}
            new[var_name] = vc
            new[value_name] = row.get(vc, '')
            out.append(new)
    return out


if __name__ == '__main__':
    headers, data, delim = parse_text(sample)
    print('Detected delimiter:', repr(delim))
    print('Headers:', headers)
    print('Data rows:', data)
    out = wide_to_long(data, 'id,name', 'subject', 'score')
    # print CSV result
    out_headers = list(out[0].keys()) if out else []
    print('\nOutput CSV:')
    print(','.join(out_headers))
    for r in out:
        print(','.join([r.get(h,'') for h in out_headers]))
