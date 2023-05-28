# Python YouTube downloader &ndash; `pytube-dlr`


## Developer road map
This project uses a combination of the MVC structure, to make every thing organized,
and the factory pattern, to make the code crossplataform. Avoid comment too much
on the body of the functions, try to document your thoughs on the docstrings, or
do some notes (like the `# todo: ...` ones) above the declaration of the function
or class. Check some notes to name things:

+ All abstract classes starts with the letter `I` to make it clear that it is a
interface.
+ All the type objects starts with `T`.

This name convention makes easy to use the classes/objects of a library by importing
specific elements of that library:

```python
# avoid
from pytube_dlr.models import types
opt: types.UserFactoryOption = 'linux_cli'

# try to do
from pytube_dlr.models.types import TUserFactoryOption
opt: TUserFactoryOption = 'linux_cli'
```


### Dependencies
+ Ripgrep (`rg`): https://github.com/BurntSushi/ripgrep
+ Poetry: https://python-poetry.org/docs/


### Commands
+ List all code todos: `rg "todo:" pytube_dlr/`
+ Run tests: `poetry run pytest -s tests/`
    + *Note: if you want to run a specific unit, specify the test file
      (all tests files follow the name `test_*.py`)*


### General todo list
+ [ ] Separate the dataclasses in `types.py` to a `dataclasses.py`
+ [ ] On the dataclasses, add a url verification (mobile, playlist, invidius)
+ [ ] Fix the sphins and make it autogenerate the documentation
    + [ ] Create a GitHub actions to publish the documentation
    + [ ] Create a GitHub actions to run the normal tests (the ones that doesn't
          test the interface looking)


