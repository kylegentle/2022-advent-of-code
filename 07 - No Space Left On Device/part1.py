#! /usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


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
        if not line.startswith("dir"):
            # File
            file = File.parse(line)
            if file not in self.files:
                self.files.append(file)
            return

        # Directory
        child = Directory.parse(line, self)
        if child in self.child_dirs:
            return

        if child.path in dirs:
            return self.child_dirs.append(dirs[child.path])

        self.child_dirs.append(child)
        dirs[child.path] = child

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

    sum_under_100k = sum((d.size() for d in dirs.values() if d.size() <= 100_000))
    print(sum_under_100k)


if __name__ == "__main__":
    main()
