import sys

pytest_plugins = 'pytester',


def test_main(testdir):
    testdir.makefile('.ini', tox=r"""[tox]
envlist = foobar
skipsdist = true

[testenv]
commands =
    python -c "import sys; print('sys.executable=%r' % sys.executable)"
    python -c "import sys; sys.stdout.write('OK\n') if {0!r}.startswith(sys.executable) or sys.executable.startswith({0!r}) else sys.stdout.write('BAD\n')"
""".format(sys.executable))

    result = testdir.run('tax', '-e', 'foobar')
    result.stdout.fnmatch_lines([
        "foobar create: *",
        "foobar installed: *",
        "foobar runtests: PYTHONHASHSEED=*",
        "foobar runtests: commands[[]0[]] | *",
        "sys.executable=*",
        "foobar runtests: commands[[]1[]] | *",
        "OK",
    ])
