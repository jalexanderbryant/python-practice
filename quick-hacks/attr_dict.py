class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

if __name__ == '__main__':
    d = AttrDict()
    .update({
        "id": 1,
        "username": "user-to-be-removed",
        "email": "remove-me@testdriven.io"
    })
    print(d)
    print(d.__dict__)

