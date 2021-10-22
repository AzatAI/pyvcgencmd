from pyvcgencmd.models import VcmdSchema, VcmdSchemaBase
from pyvcgencmd import core

vcs = VcmdSchema()


print(vcs.memory)
print(type(vcs.memory))