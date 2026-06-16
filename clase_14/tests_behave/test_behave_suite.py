import subprocess


def test_behave_smoke():

    resultado = subprocess.run(
        ["behave", "-t", "@smoke"],
        capture_output=True,
        text=True
        check=False
    )

    assert resultado.returncode == 0


def test_behave_regression():

    resultado = subprocess.run(
        ["behave", "-t", "@regression"],
        capture_output=True,
        text=True
        check=False
    )

    assert resultado.returncode == 0