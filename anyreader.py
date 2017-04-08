import json
import yaml
from io import open

from yaml.parser import ParserError


class FormatError(Exception):
    pass


class UnrecognizedFormatError(FormatError):
    pass


def anyread(filename):
    with open(filename, 'rt') as f:
        for decoder in DECODERS:
            try:
                return decoder(f)
            except FormatError:
                f.seek(0)
                continue
        else:
            raise UnrecognizedFormatError


def decoder_factory(_decoder, exception):
    def decoder(file_obj):
        try:
            return _decoder(file_obj)
        except exception:
            raise FormatError
    return decoder

json_decoder = decoder_factory(json.load, json.JSONDecodeError)
yaml_decoder = decoder_factory(yaml.load, ParserError)


DECODERS = [
    json_decoder,
    yaml_decoder
]
