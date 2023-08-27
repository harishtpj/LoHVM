# Build system for LoHVM
from invoke import task

@task
def clean(c):
    """Cleans the .pyc files generated"""
    print("Cleaning the directory")
    c.run("IF EXIST __pycache__ (del /s /q __pycache__ && rmdir __pycache__)")
    c.run("IF EXIST hvm\\__pycache__ (del /s /q hvm\\__pycache__ && rmdir hvm\\__pycache__)")
    print("Directory cleaned.")

@task(post=[clean], default=True)
def run(c):
    """Run the virtual machine."""
    print("Running the virtual machine...")
    c.run("python -O lohvm.py")
    print("*" * 10, "Program completed.", "*" * 10)

@task
def debug(c):
    """Run the virtual machine in debug mode."""
    print("Running the virtual machine in debug mode...")
    c.run("python lohvm.py")
