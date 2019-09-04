import sys
from jinja2 import Template

in_, out = sys.argv[1:]


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


lines = [i.rstrip('\r\n') for i in open(in_)]
lines = space_reveal_slides(lines)
lines = Template('\n'.join(lines))
open(out, 'w', newline='').write(lines.render(OW_ONLY=True))
