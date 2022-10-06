install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

prompt:
	poetry add prompt

make lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

package-reinstal:
	pip install --user --force-reinstall dist/*.whl
.PHONI: install build games publish prompt brain-even reinstall brain-calc
