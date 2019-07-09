import Descriptor
import Attribute
import Stat

class archetype:
    def __init__(self,identifier, args):
        self.identifier = identifier
        self.descriptors = Descriptor.descriptors()
        self.attributes = Attribute.attributes()
        self.stats = Stat.stats()
        for a in args:
            as1 = a.split(':')
            category = as1[0]
            as2 = as1[1].split('=')
            command = as2[0]
            args = as2[1]
            self.apply(category,command,args)
    def apply(self,category,command,args):
        if category == 's':
            self.stats.apply(command,args)
        elif category == 'd':
            self.descriptors.apply(command,args)
        elif category == 'a':
            self.attributes.apply(command,args)