# This file is autogenerated by the command `make fix-copies`, do not edit.
from ..file_utils import DummyObject, requires_backends


SLOW_TO_FAST_CONVERTERS = None


def convert_slow_tokenizer(*args, **kwargs):
    requires_backends(convert_slow_tokenizer, ["sentencepiece", "tokenizers"])
