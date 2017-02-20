#!/usr/bin/env python

"""
echo "SECRET_KEY = 'x'
INSTALLED_APPS = ('django.contrib.contenttypes', 'opencivicdata.apps.BaseConfig')" > settings.py
PYTHONPATH=$PYTHONPATH:$PWD DJANGO_SETTINGS_MODULE=settings ./jsonschema2rst.py
"""

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

        for key in list(keys):
            schema = obj['properties'].pop(key)
            allowed_types = []
            enum = None
            description = None
            has_properties = False
            pattern = None
            minimum = None
            minItems = None
            item_properties = None
            required = True
            nullable = None
            list_property_type = None
            list_property_enum = None
            for sk, sv in schema.items():
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
                        for ik, iv in sv.items():
                            if ik == 'type':
                                list_property_type = iv
                            elif ik == 'enum':
                                list_property_enum = iv
                elif sk == 'blank':
                    pass
                else:
                    raise ValueError('NEW KEY:', sk)

                if 'null' in allowed_types:
                    nullable = True

                if isinstance(allowed_types, list):
                    if all(isinstance(allowed_type, str) for allowed_type in allowed_types):
                        allowed_types = ', '.join(allowed_types)
                    else:
                        print('complex allowed types:', repr(allowed_types))

            spaces = '    '*depth

            # Write the property name.
            fh.write('%s**%s** ' % ('    '*(depth-1), key))

            # Write the property type, newline.
            fh.write('(*%s*)\n' % allowed_types)
            if description:
                fh.write(spaces + description)
            else:
                print('no description:', key)

            # If not an array, specify requiredness, nullability.
            if allowed_types == 'array':
                if required:
                    fh.write(' **(required, minItems: %d)**' % (minItems or 0))
            else:
                if required:
                    fh.write(' **(required)**')
            fh.write('\n')

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
                process(fh, item_properties, depth+1)
            if list_property_type:
                if isinstance(list_property_type, list):
                    list_property_type = '|'.join(list_property_type)
                fh.write(spaces + 'Each element in %s is of type (%s)' % (key, list_property_type))
                if list_property_enum is not None:
                    fh.write('\n' + spaces*2 + 'Allowed Values:\n')
                    for item in list_property_enum:
                        fh.write(spaces + '     * ' + item + '\n')
                fh.write('\n\n')

    if obj['properties']:
        print('Unused keys:', '; '.join(obj['properties'].keys()))

if __name__ == '__main__':
    import django
    django.setup()
    from pupa.scrape.schemas import vote_event, bill, event, jurisdiction, person, organization
    process(open('data/_vote.rst-include', 'w'), vote_event.schema)
    process(open('data/_bill.rst-include', 'w'), bill.schema)
    process(open('data/_event.rst-include', 'w'), event.schema)
    process(open('data/_jurisdiction.rst-include', 'w'), jurisdiction.schema)
    process(open('data/_person.rst-include', 'w'), person.schema)
    process(open('data/_organization.rst-include', 'w'), organization.schema)
