from typing import TypedDict, Unpack, Any


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]) -> Any:
    pass