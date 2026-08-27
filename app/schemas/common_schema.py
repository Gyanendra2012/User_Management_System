from typing import Annotated

from pydantic import Field

Username = Annotated[
    str,
    Field(
        min_length=3,
        max_length=50, 
    ),
]

Password = Annotated[
    str,
    Field(
        min_length=8,
        max_length=128,
    ),
]

FullName = Annotated[
    str,
    Field(
        max_length=100,
    ),
]

Mobile = Annotated[
    str,
    Field(
        max_length=20,
    ),
]

