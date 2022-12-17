#! /usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

TOTAL_SPACE = 70_000_000
FREE_SPACE_NEEDED = 30_000_000

@dataclass(eq=True)
class File:
    size: int
    name: str

    @classmethod
    def parse(cls, line: str) -> File:
        parts = line.split(" ")
        return cls(int(parts[0]), parts[1])


@dataclass(eq=True)
class Directory:
    path: str
    parent: Optional[Directory]
    files: List[File]
    child_dirs: List[Directory]

    @classmethod
    def parse(cls, line: str, pwd: Directory) -> Directory:
        parts = line.split(" ")
        return cls(f"{pwd.path}{parts[1]}/", pwd, [], [])

    def save_child(self, line: str, dirs) -> None:
        if line.startswith("dir"):
            child = Directory.parse(line, self)
            if child not in self.child_dirs:
                if child.path in dirs:
                    return self.child_dirs.append(dirs[child.path])

                self.child_dirs.append(child)
                dirs[child.path] = child
        else:
            file = File.parse(line)
            if file not in self.files:
                self.files.append(file)

    def size(self) -> int:
        return sum((f.size for f in self.files)) + sum(
            (d.size() for d in self.child_dirs)
        )


def main() -> None:
    dirs = {}
    pwd = None

    with open("input.txt", "r") as f:
        for line in f:
            l = line.strip()
            # print(dirs)
            # print(l)
            # input()
            if l == "$ cd ..":
                pwd = pwd.parent or pwd

            elif l.startswith("$ cd"):
                dir_name = l.split(" ")[-1]
                path = f"{pwd.path}{dir_name}/" if pwd else "/"
                if path not in dirs:
                    dirs[path] = Directory(path, pwd, [], [])
                pwd = dirs[path]

            elif l.startswith("$ ls"):
                continue

            else:
                dirs[pwd.path].save_child(l, dirs)

    used_space = dirs["/"].size()
    print(used_space)

    min_ = float('inf')
    space_to_free = FREE_SPACE_NEEDED - (TOTAL_SPACE - used_space)
    print(space_to_free)
    for d in dirs.values():
        if (s := d.size()) >= space_to_free:
            min_ = min(min_, s)
    print(min_)


if __name__ == "__main__":
    main()
