from typing import BinaryIO
from typing_extensions import TypeAlias

__all__ = ["Error", "encode", "decode"]

_File: TypeAlias = str | BinaryIO

class Error(Exception): ...

def encode(
    in_file: _File, out_file: _File, name: str | None = None, mode: int | None = None, *, backtick: bool = False
) -> None: ...
def decode(in_file: _File, out_file: _File | None = None, mode: int | None = None, quiet: bool = False) -> None: ...
