from dataclasses import dataclass

from seaborn._marks.base import MappableBool, MappableColor, MappableFloat, MappableStyle, Mark, document_properties

class BarBase(Mark): ...

@document_properties
@dataclass
class Bar(BarBase):
    color: MappableColor = ...
    alpha: MappableFloat = ...
    fill: MappableBool = ...
    edgecolor: MappableColor = ...
    edgealpha: MappableFloat = ...
    edgewidth: MappableFloat = ...
    edgestyle: MappableStyle = ...
    width: MappableFloat = ...
    baseline: MappableFloat = ...

@document_properties
@dataclass
class Bars(BarBase):
    color: MappableColor = ...
    alpha: MappableFloat = ...
    fill: MappableBool = ...
    edgecolor: MappableColor = ...
    edgealpha: MappableFloat = ...
    edgewidth: MappableFloat = ...
    edgestyle: MappableStyle = ...
    width: MappableFloat = ...
    baseline: MappableFloat = ...
