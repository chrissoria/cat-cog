"""Back-compat alias for `catcog`.

The canonical import name is `catcog`. `cat_cog` is retained so existing
code continues to work; prefer `catcog` in new code.
"""
import importlib
import sys

_canonical = "catcog"
_real = importlib.import_module(_canonical)

sys.modules[__name__] = _real

_src_prefix = _canonical + "."
_dst_prefix = __name__ + "."
for _name in list(sys.modules):
    if _name.startswith(_src_prefix):
        sys.modules[_dst_prefix + _name[len(_src_prefix):]] = sys.modules[_name]
