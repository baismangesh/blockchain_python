class Food:

    # name
    # kind
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def __repr__(self):
        return 'name: {}, kind: {} '.format(
            self.name, 
            self.kind
        )

    def describe(self):
        print('Name: ', self.name)
        print('Kind: ', self.kind)

    # @classmethod
    # def describe(cls):
    #     print('Name: ', cls.name)
    #     print('Kind: ', cls.kind)

    # @staticmethod
    # def describe(cls):
    #     print('Name: ', name)
    #     print('Kind: ', kind)