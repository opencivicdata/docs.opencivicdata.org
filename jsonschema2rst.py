#!/usr/bin/env python

from __future__ import print_function
import copy

HEADER_SYMBOL = "=-*~'"

def process(fh, obj, depth=1):
    obj = copy.deepcopy(obj)
    if '_order' in obj:
        _order = obj['_order']
    else:
        _order = ((None, obj['properties'].keys()),)

    for section, keys in _order:

        if section:
            fh.write('%s\n%s\n\n' % (section, HEADER_SYMBOL[depth]*len(section)))

        for key in keys:
            schema = obj['properties'].pop(key)
            allowed_types = []
            enum = None
            description = None
            has_properties = False
            pattern = None
            minimum = None
            minItems = None
            item_properties = None
            required = None
            for sk, sv in schema.iteritems():
                if sk == 'type':
                    allowed_types = sv
                elif sk == 'enum':
                    enum = sv
                elif sk == 'description':
                    description = sv
                elif sk == 'properties':
                    has_properties = True
                elif sk == 'pattern':
                    pattern = sv
                elif sk == 'minimum':
                    minimum = sv
                elif sk == 'minItems':
                    minItems = sv
                elif sk == 'required':
                    required = sv
                elif sk in ('format', 'maximum', 'minimum'):
                    pass
                elif sk in ('items', 'additionalProperties'):
                    if 'properties' in sv:
                        item_properties = sv
                    else:
                        pass # maybe put something here
                else:
                    raise ValueError('NEW KEY:', sk)

                if isinstance(allowed_types, list):
                    allowed_types = ', '.join(allowed_types)

            spaces = '    '*depth
            fh.write('%s**%s**\n' % ('    '*(depth-1), key))
            if description:
                fh.write(spaces + description)
            if required:
                fh.write(' (Required)')
            if nullable:
                fh.write(spaces + ' (Nullable)')
            fh.write('\n')
            else:
                print('no description:', key)
            #'\n' + spaces + 'Allowed Types: ' + allowed_types
            if enum is not None:
                fh.write('\n' + spaces + 'Allowed Values:\n')
                for item in enum:
                    fh.write(spaces + '     * ' + item + '\n')
            if minimum is not None:
                fh.write('\n' + spaces + '(minimum value: %s)\n' % minimum)
            if pattern is not None:
                fh.write('\n'+ spaces + '(must match format: ``%s``)\n' % pattern)
            fh.write('\n\n')
            if has_properties:
                process(fh, schema, depth+1)
            if item_properties:
                fh.write(spaces + 'Each element in %s is an object with the following keys: \n\n'
                         % key)
                print(key, item_properties)
                process(fh, item_properties, depth+1)

    if obj['properties']:
        print('Unused keys:', '; '.join(obj['properties'].keys()))

if __name__ == '__main__':
    from pupa.models.schemas import vote, bill, event, jurisdiction, person, organization
    process(open('data/_vote.rst-include', 'w'), vote.schema)
    process(open('data/_bill.rst-include', 'w'), bill.schema)
    process(open('data/_event.rst-include', 'w'), event.schema)
    process(open('data/_jurisdiction.rst-include', 'w'), jurisdiction.schema)
    process(open('data/_person.rst-include', 'w'), person.schema)
    process(open('data/_organization.rst-include', 'w'), organization.schema)
