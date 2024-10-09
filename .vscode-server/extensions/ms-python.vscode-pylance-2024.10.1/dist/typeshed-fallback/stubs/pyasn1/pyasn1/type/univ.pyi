from _typeshed import ConvertibleToInt, Incomplete, SupportsRichComparison
from collections.abc import Callable, Generator
from typing_extensions import Self

from pyasn1.type import base, constraint, namedtype, namedval
from pyasn1.type.tag import TagSet

__all__ = [
    "Integer",
    "Boolean",
    "BitString",
    "OctetString",
    "Null",
    "ObjectIdentifier",
    "Real",
    "Enumerated",
    "SequenceOfAndSetOfBase",
    "SequenceOf",
    "SetOf",
    "SequenceAndSetBase",
    "Sequence",
    "Set",
    "Choice",
    "Any",
    "NoValue",
    "noValue",
]

NoValue = base.NoValue
noValue: NoValue

class Integer(base.SimpleAsn1Type):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    namedValues: namedval.NamedValues
    typeId: int
    def __init__(self, value=..., **kwargs) -> None: ...
    def __and__(self, value): ...
    def __rand__(self, value): ...
    def __or__(self, value): ...
    def __ror__(self, value): ...
    def __xor__(self, value): ...
    def __rxor__(self, value): ...
    def __lshift__(self, value): ...
    def __rshift__(self, value): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __sub__(self, value): ...
    def __rsub__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __mod__(self, value): ...
    def __rmod__(self, value): ...
    # Accepts everything builtins.pow does
    def __pow__(self, value: complex, modulo: int | None = None) -> Self: ...
    def __rpow__(self, value): ...
    def __floordiv__(self, value): ...
    def __rfloordiv__(self, value): ...
    def __truediv__(self, value): ...
    def __rtruediv__(self, value): ...
    def __divmod__(self, value): ...
    def __rdivmod__(self, value): ...
    __hash__ = base.SimpleAsn1Type.__hash__
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __abs__(self): ...
    def __index__(self) -> int: ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __invert__(self): ...
    def __round__(self, n: int = 0): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __trunc__(self): ...
    def __lt__(self, value): ...
    def __le__(self, value): ...
    def __eq__(self, value): ...
    def __ne__(self, value): ...
    def __gt__(self, value): ...
    def __ge__(self, value): ...
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...
    def getNamedValues(self): ...

class Boolean(Integer):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    namedValues: namedval.NamedValues
    typeId: int

SizedIntegerBase = int

class SizedInteger(SizedIntegerBase):
    bitLength: int | None
    leadingZeroBits: int | None
    def setBitLength(self, bitLength): ...
    def __len__(self) -> int: ...

class BitString(base.SimpleAsn1Type):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    namedValues: namedval.NamedValues
    typeId: int
    defaultBinValue: str | base.NoValue
    defaultHexValue: str | base.NoValue
    def __init__(self, value=..., **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __reversed__(self): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __lshift__(self, count): ...
    def __rshift__(self, count): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def asNumbers(self): ...
    def asOctets(self): ...
    def asInteger(self): ...
    def asBinary(self): ...
    @classmethod
    def fromHexString(cls, value, internalFormat: bool = False, prepend: ConvertibleToInt | None = None): ...
    @classmethod
    def fromBinaryString(cls, value, internalFormat: bool = False, prepend: ConvertibleToInt | None = None): ...
    @classmethod
    def fromOctetString(cls, value, internalFormat: bool = False, prepend: ConvertibleToInt | None = None, padding: int = 0): ...
    def prettyIn(self, value): ...

class OctetString(base.SimpleAsn1Type):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    defaultBinValue: str | base.NoValue
    defaultHexValue: str | base.NoValue
    encoding: str
    def __init__(self, value=..., **kwargs) -> None: ...
    def prettyIn(self, value): ...
    def __bytes__(self) -> bytes: ...
    def asOctets(self): ...
    def asNumbers(self): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = 0): ...
    @staticmethod
    def fromBinaryString(value): ...
    @staticmethod
    def fromHexString(value): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __reversed__(self): ...

class Null(OctetString):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    def prettyIn(self, value): ...

class ObjectIdentifier(base.SimpleAsn1Type):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def asTuple(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def index(self, suboid): ...
    def isPrefixOf(self, other): ...
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...

class Real(base.SimpleAsn1Type):
    binEncBase: int | None
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    def prettyIn(self, value): ...
    def prettyPrint(self, scope: int = 0): ...
    @property
    def isPlusInf(self): ...
    @property
    def isMinusInf(self): ...
    @property
    def isInf(self): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __sub__(self, value): ...
    def __rsub__(self, value): ...
    def __mod__(self, value): ...
    def __rmod__(self, value): ...
    # Accepts everything builtins.pow with a float base does
    def __pow__(self, value: complex, modulo: int | None = None) -> Self: ...
    def __rpow__(self, value): ...
    def __truediv__(self, value): ...
    def __rtruediv__(self, value): ...
    def __divmod__(self, value): ...
    def __rdivmod__(self, value): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __abs__(self): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __round__(self, n: int = 0): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __trunc__(self): ...
    def __lt__(self, value): ...
    def __le__(self, value): ...
    def __eq__(self, value): ...
    def __ne__(self, value): ...
    def __gt__(self, value): ...
    def __ge__(self, value): ...
    def __bool__(self) -> bool: ...
    __hash__ = base.SimpleAsn1Type.__hash__
    def __getitem__(self, idx): ...
    def isPlusInfinity(self): ...
    def isMinusInfinity(self): ...
    def isInfinity(self): ...

class Enumerated(Integer):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    namedValues: namedval.NamedValues

class SequenceOfAndSetOfBase(base.ConstructedAsn1Type):
    componentType: namedtype.NamedTypes | None
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    def __init__(
        self,
        *args,
        componentType: namedtype.NamedTypes | None = ...,
        tagSet: TagSet = ...,
        subtypeSpec: constraint.ConstraintsIntersection = ...,
    ) -> None: ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, value) -> None: ...
    def append(self, value) -> None: ...
    def count(self, value): ...
    def extend(self, values) -> None: ...
    def index(self, value, start: int = 0, stop: int | None = None): ...
    def reverse(self) -> None: ...
    def sort(self, key: Callable[[Incomplete], SupportsRichComparison] | None = None, reverse: bool = False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = True): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = True, matchTags: bool = True, matchConstraints: bool = True
    ): ...
    @property
    def componentTagMap(self): ...
    @property
    def components(self): ...
    def clear(self): ...
    def reset(self): ...
    def prettyPrint(self, scope: int = 0): ...
    def prettyPrintType(self, scope: int = 0): ...
    @property
    def isValue(self): ...
    @property
    def isInconsistent(self): ...

class SequenceOf(SequenceOfAndSetOfBase):
    typeId: int

class SetOf(SequenceOfAndSetOfBase):
    typeId: int

class SequenceAndSetBase(base.ConstructedAsn1Type):
    componentType: namedtype.NamedTypes

    class DynamicNames:
        def __init__(self) -> None: ...
        def __len__(self) -> int: ...
        def __contains__(self, item) -> bool: ...
        def __iter__(self): ...
        def __getitem__(self, item): ...
        def getNameByPosition(self, idx): ...
        def getPositionByName(self, name): ...
        def addField(self, idx) -> None: ...

    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def values(self) -> Generator[Incomplete, None, None]: ...
    def keys(self): ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def update(self, *iterValue, **mappingValue) -> None: ...
    def clear(self): ...
    def reset(self): ...
    @property
    def components(self): ...
    def getComponentByName(self, name, default=..., instantiate: bool = True): ...
    def setComponentByName(
        self, name, value=..., verifyConstraints: bool = True, matchTags: bool = True, matchConstraints: bool = True
    ): ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = True): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = True, matchTags: bool = True, matchConstraints: bool = True
    ): ...
    @property
    def isValue(self): ...
    @property
    def isInconsistent(self): ...
    def prettyPrint(self, scope: int = 0): ...
    def prettyPrintType(self, scope: int = 0): ...
    def setDefaultComponents(self): ...
    def getComponentType(self): ...
    def getNameByPosition(self, idx): ...

class Sequence(SequenceAndSetBase):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    componentType: namedtype.NamedTypes
    typeId: int
    def getComponentTagMapNearPosition(self, idx): ...
    def getComponentPositionNearType(self, tagSet, idx): ...

class Set(SequenceAndSetBase):
    tagSet: TagSet
    componentType: namedtype.NamedTypes
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    def getComponent(self, innerFlag: bool = False): ...
    def getComponentByType(self, tagSet, default=..., instantiate: bool = True, innerFlag: bool = False): ...
    def setComponentByType(
        self,
        tagSet,
        value=...,
        verifyConstraints: bool = True,
        matchTags: bool = True,
        matchConstraints: bool = True,
        innerFlag: bool = False,
    ): ...
    @property
    def componentTagMap(self): ...

class Choice(Set):
    tagSet: TagSet
    componentType: namedtype.NamedTypes
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...
    def values(self) -> Generator[Incomplete, None, None]: ...
    def keys(self) -> Generator[Incomplete, None, None]: ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def checkConsistency(self) -> None: ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = True): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = True, matchTags: bool = True, matchConstraints: bool = True
    ): ...
    @property
    def effectiveTagSet(self): ...
    @property
    def tagMap(self): ...
    def getComponent(self, innerFlag: bool = False): ...
    def getName(self, innerFlag: bool = False): ...
    @property
    def isValue(self): ...
    def clear(self): ...
    def getMinTagSet(self): ...

class Any(OctetString):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int
    @property
    def tagMap(self): ...
