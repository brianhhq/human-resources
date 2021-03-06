# HR
CLI for manage users on a server based on an “inventory” JSON file


## Preparing for Development

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/hr``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``


## Usage

Create user via a json file
```
$ hr path/to/inventory.json
```

Alternative
```
$ hr --export path/to/inventory.json
```


## Running Tests

Run tests locally using ``make`` if virtualenv is active:
```
  $ make
```

If virtualenv isn’t active then use:
```
$ pipenv run make
```

