import Archetype
from Archetype import Descriptor, Attribute, Stat

class entity:
    def __init__(self, name, archetype, args):
        self.name = name
        self.archetype = archetype
        if archetype:
            self.identifier = self.archetype.identifier
        else:
            self.identifier = name
        self.subentities = []
        
        if archetype:
            self.descriptors = self.archetype.descriptors
            self.attributes = self.archetype.attributes
            self.stats = self.archetype.stats
        else:
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