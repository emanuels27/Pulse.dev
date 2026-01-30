import os
from collections import Counter


def analyze_project(path="."):
    folders = 0
    files = 0
    size = 0
    extensions = Counter()

    for root, dirs, filenames in os.walk(path):
        folders += len(dirs)
        for file in filenames:
            files += 1
            filepath = os.path.join(root, file)

            try:
                size += os.path.getsize(filepath)
            except OSError:
                pass

            ext = os.path.splitext(file)[1] or "sem_ext"
            extensions[ext] += 1

    return {
        "folders": folders,
        "files": files,
        "size_kb": size / 1024,
        "extensions": extensions.most_common(5),
    }


def analyze_python(path="."):
    py_files = 0
    py_lines = 0
    py_functions = 0
    py_classes = 0

    for root, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(".py"):
                py_files += 1
                filepath = os.path.join(root, file)

                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            py_lines += 1
                            line_strip = line.strip()
                            if line_strip.startswith("def "):
                                py_functions += 1
                            elif line_strip.startswith("class "):
                                py_classes += 1
                except OSError:
                    pass

    return {
        "files": py_files,
        "lines": py_lines,
        "functions": py_functions,
        "classes": py_classes,
    }
