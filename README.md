# py-template
A templating language for embedding python in source files


# Why?

This is a templating solution for embedded python expressions and source in C files.
This can be a clean way of injecting some compile-time logic into a program - where the python source is inline with your source - making it pretty easy to get a full understanding of whats going on.

# Usage

## Basic

Given a source file named `file.c.tmpl`
```txt
const char * number = "${{10 + 63}}"
```

The templater is run using: `python template.py file.c.tmpl`

The output file will be `file.c`
```c
const char * number = "73"
```

## Expressions & Execution

All expressions within `${{...}}` are evaluated as a python expression.

All expressions within `!{{...}}` are executed. Variables from an executed block can be referenced in subsequent expressions.

For example:

```txt
!{{
import subprocess

def Cmd(command):
    return subprocess.check_output(command).decode('ascii').strip()

REV = Cmd("git rev-parse --short HEAD")
}}

const char * revision = "${{REV}}"
```

Compiles to:

```c
const char * revision = "f6335a7"
```

## Output path

By default the output path will be the input path minus the `.tmpl` file extention. This can also be passed explicitly:

`python template.py file.c.tmpl output/file.c`