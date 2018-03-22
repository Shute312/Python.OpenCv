from enum import Enum,unique

@unique
class ControlType(Enum):
    Button=1,
    Input=2,
    TrackBar=3,
    SelectBox=4,
    CheckBox=5,
    Image=6,