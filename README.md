# Pymodel

An example of a Python ML model serving app running as a gRPC server. Plus a Go client with a static request data.

## How to Run

*We're using [mage](https://magefile.org/) as a command runner.*

1. (Optional) Create Python virtual env and activate it: `pyenv virtualenv <python version> <venv name> && pyenv local <venv name>`
1. Install requirements: `pip install -r py/requirements.txt`
1. (Optional) Re-train the model: `python py/train.py`. The serialized model should appear as in `py/model.joblib`
1. Generate proto code: `mage generateProtoGo && mage generateProtoPy`
1. Start a Python model server in one terminal: `mage runPyServer`
1. Get predictions in another terminal: `mage getPredictions`