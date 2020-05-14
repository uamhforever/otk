# otk - optics toolkit

Toolkit for doing optics in Python

<img src="screenshots/zemax_conic_telecentric_lens.png" width="400  " title="conic telecentric lens with rays"><img src="screenshots/cell-phone-lens.png" width="160" title="cell phone lens"><img src="screenshots/csg.png" width="160" title="cell phone lens">

Features include

* 3D engine based on [sphere tracing](https://link.springer.com/article/10.1007/s003710050084) for simple robust implicit surfaces and constructive solid geometry,
* nonsequential ray tracing engine,
* programmatic lookup of full [RefractiveIndex.INFO](https://refractiveindex.info/) database,
* import of lenses and glass catalogs from Zemax.

## Installation

Installation methods include:

* Clone repository and interact with it using [Poetry](https://python-poetry.org/) e.g. `poetry run view-zmx <zemax-file>` or `poetry shell`.
* Install in development mode with pip: `pip install -e <path-to-local-repo>`.
* Install from package repository (e.g. PyPi) with pip: `pip install otk`.
* Development mode with [: `poetry add <path-to-local-repo>`.
* From package repository (e.g. PyPi) with Poetry: `poetry add otk`.

## Getting started

1. Check out the scripts in [examples](./examples).
2. View one of the lenses in [designs](./designs) with the command line tool `view-zmx`.

## Documentation

(Yep, this is it at the moment.)

### Command line tools

`view-zmx <zemaxfile>` launches a viewer of a Zemax lens.

### Packages

* `otk.sdb` - Geometry library based on signed distance bounds.
* `otk.rt1` - First attempt at ray tracing package. Superseded by otk.rt2.
* `otk.rt2` - Ray tracing package with flexible geometry based on otk.sdb. See also `otk.rt2_scalar_qt`.
* `otk.asbp` - Angular spectrum beam propagation.
* `otk.abcd` - 1D ray transfer matrix ("ABCD matrices") tools.
* `otk.rtm4` - abstractions for 1D ray transfer matrices, building upon `otk.abcd`.
* `otk.pgb` - parabasal Gaussian routines for doing wave optical calculations with ray tracing results. Builds upon `otk.rt1`.
* `otk.h4t` - homogeneous 4x4 transformation matrices.
* `otk.paraxial` - basic paraxial optics calculations.
* `otk.math` - various optics-specific math functions.
* `otk.pov` - tools for generating POV-Ray scenes of optical setups.
* `otk.pov` - for calculating properties of prisms.
* `otk.qt` - Qt-related utilities
* `otk.ri` - refractive index tools.
* `otk.trains` - axially symmetric optical systems
* `otk.v3` - operations on homogeneous vectors in 2D
* `otk.v4` - operations on homogeneous vectors in 3D
* `otk.v4b` - broadcasting operations on homogeneous vectors in 3D
* `otk.zemax` - reading Zemax files

## Folder contents

* `otk` - the Python package itself.
* `examples` - example scripts.
* `properties` - material properties databases.
* `notes` - miscellaneous notes including derivations.

## Package management

otk uses [Poetry](https://python-poetry.org/) for package management. This means that dependencies, version, entry points etc are all defined in [`pyproject.toml`](./pyproject.toml). [`setup.py`](./setup.py) is generated using `dephell deps convert` to support pip development mode installation.

### Using [PyPi test instance](test.pypi.org)

To setup, add test.pypi.org to your Poetry configuration with `poetry config repositories.test https://test.pypi.org/legacy/`. Note the [trailing slash](https://github.com/python-poetry/poetry/issues/742).

To publish (after `poetry build`), `poetry publish -r test`.

To test that it installs properly,
1. create and activate a virtual environment, and
2. per [instructions](https://packaging.python.org/guides/using-testpypi/), `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple otk`.

## Contributing

Please do.

Test framework uses `pytest` and `pytest-qt`.
