import re
import sys
from itertools import chain
from types import SimpleNamespace
from jinja2 import Template

Slide = SimpleNamespace
in_, out = sys.argv[1:]

tags_re = re.compile(r"<!--.*\.tags:\s*([A-Za-z_][-, A-Za-z_0-9]*)")
comma_re = re.compile(r"\s*,\s*")


def get_slides(text):
    out = [Slide(level=0, body=[], tags=set())]
    in_ticks = False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_ticks = ~in_ticks
        if line.startswith('#') and not in_ticks:
            out.append(
                Slide(
                    level=len(line) - len(line.lstrip('#')),
                    body=[line],
                    tags=set(),
                )
            )
        else:
            # append the line if it's non-blank or one of the last two
            # lines of the body is non-blank
            if line.strip() or ''.join(out[-1].body[-2:]).strip():
                out[-1].body.append(line)
        tags = tags_re.search(line)
        if tags:
            out[-1].tags.update(comma_re.split(tags[1].rstrip(' -')))

    return out


tags_required = set(['pf'])
tags_exclude = set()

text = open(in_).read().replace('\r', '')
slides = get_slides(text)
if tags_required:
    slides = [i for i in slides if i.tags & tags_required or i.level == 0]
slides = [i for i in slides if not (i.tags & tags_exclude) or i.level == 0]


def space_reveal_slides(lines):
    new = []
    in_ticks = False

    for line in lines:
        if line.strip().startswith('```'):
            in_ticks = ~in_ticks
        if new and line.startswith('#') and not in_ticks:
            tail = [''] * min(3, 5 - (1 + len(line) - len(line.lstrip('#'))))
            # or tail = ['']*min(3, 1+len(line)-len(line.lstrip('#'))) ?
            while new[-len(tail) :] != tail:
                new.append('')
            new.append(line)
        elif line.strip() or new and new[-1].strip():
            new.append(line)
    return new


lines = ''.join(chain('\n'.join(i.body)+'\n' for i in slides))
# lines = '\n'.join([i.rstrip('\r\n') for i in open(in_)])
context = {'SUMMARY': True, 'OW_ONLY': False}
open(out+'.tmpl', 'w').write(lines)
lines = Template(lines).render(**context).split('\n')
lines = space_reveal_slides(lines)
lines = '\n'.join(lines)
open(out, 'w', newline='').write(lines)
