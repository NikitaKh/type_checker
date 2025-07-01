from typing import NotRequired, TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]
