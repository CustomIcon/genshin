import json

from typing import Tuple, List, Set, Union, Dict, Any

# Dragsama's code
class Attrify(dict):
    def __init__(self, *args, **kwargs):
        cdict = args[0] if args else kwargs
        for key in cdict:
            if isinstance(cdict[key], dict):
                cdict[key] = Attrify(cdict[key])
            elif isinstance(cdict[key], (list, tuple, set)):
                cdict[key] = self.convert_list(cdict[key])
        super().__init__(*args, **cdict)

    def convert_list(self, n: Union[List[Any], Tuple[Any, ...], Set[Any]]) -> List[Any]:
        new_list = []
        for item in n:
            if isinstance(item, (list, tuple, set)):
                new_list.append(self.convert_list(item))
            elif isinstance(item, dict):
                new_list.append(Attrify(item))
            else:
                new_list.append(item)
        return new_list

    def to_dict(self) -> Dict[str, Any]:
        _dict = dict(self)
        for key, value in _dict.items():
            if isinstance(_dict[key], Attrify):
                _dict[key] = _dict[key].to_dict()
            elif isinstance(value, (list, tuple, set)):
                new_list = []
                for i in _dict[key]:
                    if isinstance(i, Attrify):
                        new_list.append(i.to_dict())
                    else:
                        new_list.append(i)
                _dict[key] = new_list
        return _dict

    def prettify(self, indent:int=4) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def __getattr__(self, attr) -> Any:
        if attr in self:
            return self[attr]
        raise AttributeError(f"Attrify has no attribute '{attr}'")

    def __dir__(self) -> List[str]:
        l = dict.__dir__(self)
        # Add all keys that are alphabetic. 
        l.extend([x for x in self.keys() if str(x).isalpha()])
        return l


def pretty(value, htchar='\t', lfchar='\n', indent=0):
    nlch = lfchar + htchar * (indent + 1)
    if type(value) is dict:
        items = [
            nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is list:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is tuple:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
    else:
        return repr(value)