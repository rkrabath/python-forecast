PYTHON = $(shell which python3.5)

env: env/bin/activate
	@echo ""
	@echo "=========="
	@echo "Please run the following command before continuing:"
	@echo "source env/bin/activate"
	@echo "=========="

env/bin/activate: requirements.txt
	test -d env || virtualenv --python=$(PYTHON) --system-site-packages env
	env/bin/pip install -Ur requirements.txt
	touch env/bin/activate

