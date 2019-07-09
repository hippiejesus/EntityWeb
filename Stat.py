import Action

class stats:
    def __init__(self):
        self.list = []
        
    def apply(self, command, args):
        asplit = args.split('|')
        coms = { '+' : self.add,
                 '-' : self.remove,
                 '!' : self.set,
                 'r' : self.ret}
        return coms[command](asplit)
        
    def add(self, args):
        name = args[0]
        value = args[1]
        self.list.append(stat(name,value))
        return True
        
    def remove(self, args):
        newlist = []
        for a in self.list:
            if a.name == args[0]:
                pass
            else:
                newlist.append(a)
        self.list = newlist
        return True
        
    def set(self,args):
        target = self.list[args[0]]
        target.set_value(args[1])
        return True
        
    def ret(self, args):
        returnlist = []
        if args != []:
            for a in args:
                for i in self.list:
                    if i.name == a:
                        returnlist.append(i)
        else:
            returnlist = self.list
        return returnlist
        
class stat:
    def __init__(self, name, default_value):
        self.name = name
        self.value = default_value
        self.action = Action.action()
    def set_value(self, value):
        self.value = value