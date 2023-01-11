from invoke import task

@task
def hi(c):
    print("Hi")

@task
def setup(c):
    print("[INFO] Setup")
    c.run("mkdir input")
    c.run("mkdir output")

@task
def clear(c):
    print("[INFO] Clear")
    c.run("rm -rf input")
    c.run("rm -rf output")
    c.run("rm -rf _build")

@task
def html(c):
    print("[INFO] Make HTML")
    c.run("make html")

@task
def full(c):
    print("[INFO] Full run")
    clear(c)
    setup(c)
    html(c)
