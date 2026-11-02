import subprocess


def run(user_input):
    subprocess.run(user_input, shell=True)


def calc(expr):
    return eval(expr)
