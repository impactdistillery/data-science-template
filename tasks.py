from invoke import task
import conf

@task
def hi(c):
    print("Welcome to the ADS demo project.")

@task
def download_data(c):
    print("[INFO] Download data")
    c.run(f"cd input && wget {conf.data_url}")

@task
def setup(c):
    print("[INFO] Setup")
    c.run("mkdir input")
    c.run("mkdir output")
    c.run("mkdir temp")
    download_data(c)

@task
def clear(c):
    print("[INFO] Clear")
    c.run("rm -rf input")
    c.run("rm -rf output")
    c.run("rm -rf temp")
    c.run("rm -rf _build")

@task
def apidoc(c):
    print("[INFO] Create apidoc")
    c.run("sphinx-apidoc lib_py -o temp/apidoc")

@task
def html(c):
    print("[INFO] Make HTML")
    c.run("make html")

@task
def full(c):
    print("[INFO] Full run")
    clear(c)
    setup(c)
    apidoc(c)
    html(c)
