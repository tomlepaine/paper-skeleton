from invoke import run, task

@task
def clean():
    patterns = []
    patterns.append('*.aux')
    patterns.append('*.bbl')
    patterns.append('*.blg')
    patterns.append('*.bbl')
    patterns.append('*.dtx')
    patterns.append('*.ins')
    patterns.append('*.fd')
    patterns.append('*.dvi')
    patterns.append('*.pdf')
    patterns.append('*.log')
    patterns.append('*.toc')
    patterns.append('*.lof')
    patterns.append('*.lot')
    patterns.append('*.idx')
    patterns.append('*.ind')
    patterns.append('*.ilg')
    patterns.append('*.out')
    patterns.append('*.txt')
    patterns.append('*.gz')
    patterns.append('*.pyc')
    patterns.append('*.fls')
    patterns.append('*latexmk')
    for pattern in patterns:
        run("rm -rf %s" % pattern)

@task
def make():
    run("latexmk -pdf main.tex")

@task
def open():
    run("open main.pdf")