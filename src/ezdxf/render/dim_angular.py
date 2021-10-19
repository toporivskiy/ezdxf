# Copyright (c) 2021, Manfred Moitzi
# License: MIT License
from typing import TYPE_CHECKING
from ezdxf.math import Vec3, Vec2, UCS
from ezdxf.entities.dimstyleoverride import DimStyleOverride
from .dim_base import BaseDimensionRenderer

if TYPE_CHECKING:
    from ezdxf.eztypes import Dimension, Vertex, GenericLayoutType


class AngularDimension(BaseDimensionRenderer):
    """
    Angular dimension line renderer.

    Supported render types:

    - default location above
    - default location center
    - user defined location, text aligned with dimension line
    - user defined location horizontal text

    Args:
        dimension: DXF entity DIMENSION
        ucs: user defined coordinate system
        override: dimension style override management object

    """
    pass

