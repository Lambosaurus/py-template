#!/usr/bin/python

# Source:
# https://github.com/Lambosaurus/py-template.git

import sys

def format(result):
    if type(result) == bool:
        # lowercase booleans
        return "true" if result else "false"
    return str(result)

def substitute(subs, params):
    outputs = {}
    exec("result = " + subs, params, outputs)
    return format(outputs["result"])

def execute(subs, params):
    exec(subs, params, params)
    return ""

def run_template(content, start_marker, end_marker, evaluator):
    chunks = content.split(start_marker)
    for i in range(1, len(chunks)):
        chunk = chunks[i]
        end = chunk.find(end_marker)
        if end == -1:
            continue
        subs = chunk[0:end]
        tail = chunk[end+len(end_marker):]
        chunks[i] = evaluator(subs) + tail
    return "".join(chunks)

def template_content(content, params):
    content = run_template(content, "!{{", "}}", lambda text: execute(text, params))
    content = run_template(content, "${{", "}}", lambda text: substitute(text, params))
    return content

def template_file(src_path, dst_path, params = {}):
    with open(src_path, 'r') as src:
        content = src.read()

    content = template_content(content, params)

    with open(dst_path, 'w') as dst:
        dst.write(content) 

if __name__ == "__main__":

    src_path = sys.argv[1]

    if len(sys.argv) > 2:
        dst_path = sys.argv[2]
    else:
        # if no destination is specified, just try remove the .tmpl file extention
        dst_path = src_path.replace(".tmpl", "")

    template_file(src_path, dst_path)
    
