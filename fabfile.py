from fabric.api import local,lcd


def build():
    local("copy README.md docs\index.md")
    local("mkdocs build")
    with lcd("..\East196.github.io"):
        local("rd /s /q oxdeepnlp")
    local("xcopy site ..\East196.github.io\oxdeepnlp\ /s /e")


def serve():
    local("mkdocs serve")
