class MixinLog:

    def __init__(self, *args,**kwargs):
        print(self.__repr__())
