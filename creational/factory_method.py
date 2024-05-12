from abc import ABC, abstractmethod


class Encoder(ABC):
    """ ABSTRACT CREATOR """

    @abstractmethod
    def encode(self, txt: str):
        ...

    @abstractmethod
    def create_file(self):
        ...


class JsonEncoder(Encoder):
    """ CONCRETE CREATOR """

    def encode(self, txt: str):
        return f'JSON {txt}'

    def create_file(self):
        return 'JSON file created'


class XmlEncoder(Encoder):
    """ CONCRETE CREATOR """

    def encode(self, txt: str):
        return f'XML {txt}'

    def create_file(self):
        return 'XML file created'


def create_encoder(encoder: str):
    _encoders = {
        'JSON': JsonEncoder,
        'XML': XmlEncoder
    }
    return _encoders[encoder]()


def test():
    _txts = ['Hello', 'World']
    _json_encoder = create_encoder('JSON')
    _xml_encoder = create_encoder('XML')
    for txt in _txts:
        _json_encoder.encode(txt)
        _xml_encoder.encode(txt)
        _json_encoder.create_file()
        _xml_encoder.create_file()
