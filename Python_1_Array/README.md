# Python environment setup

This project requires **Python 3.10**.

## 1. Check if pyenv is installed

Check whether `pyenv` is available:

```bash
pyenv --version
```

If you get:

```text
bash: pyenv: command not found
```

install `pyenv` in your home directory:

```bash
curl https://pyenv.run | bash
```

No `sudo` is required.

## 2. Configure pyenv in Bash

Add the following lines to `~/.bashrc`:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

Reload the Bash configuration:

```bash
source ~/.bashrc
```

Verify that `pyenv` is available:

```bash
pyenv --version
```

## 3. Install Python 3.10

Install Python 3.10 with `pyenv`:

```bash
pyenv install 3.10.18
```

Check the installed versions:

```bash
pyenv versions
```

## 4. Select Python 3.10 for the project

From the project directory:

```bash
pyenv local 3.10.18
```

This creates a `.python-version` file in the project directory.

Verify:

```bash
python --version
```

Expected:

```text
Python 3.10.18
```

## 5. Create a virtual environment

Create the virtual environment using Python 3.10:

```bash
python -m venv myenv
```

## 6. Activate the virtual environment

```bash
source myenv/bin/activate
```

Verify the Python version:

```bash
python --version
```

Expected:

```text
Python 3.10.18
```

Check the Python executable:

```bash
which python
```

It should point to:

```text
.../myenv/bin/python
```

## 7. Upgrade pip

```bash
python -m pip install --upgrade pip
```

If you see:

```text
WARNING: There was an error checking the latest version of pip
```

this usually means that `pip` could not contact PyPI to check for a newer version. This warning does not necessarily indicate a problem with the environment.

## 8. Install requirements

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## 9. Create or update requirements.txt

After installing or changing dependencies:

```bash
pip freeze > requirements.txt
```

## 10. Deactivate the virtual environment

When you are finished working:

```bash
deactivate
```

## 11. Reactivate the environment

When returning to the project:

```bash
cd /path/to/project
source myenv/bin/activate
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.10.18
```

## Notes

- The project requires **Python 3.10**.
- `pyenv` manages the Python version without modifying the system Python.
- `myenv` is the project's virtual environment.
- `requirements.txt` contains the project's dependencies.