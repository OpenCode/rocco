# ROCCO: the Rapsodoo Original CookieCutter for Odoo
## A long and durable piece of software

ROCCO is your swiss-army knife to build Docker Environments for Odoo. It has been designed to replicate odoo.sh projects locally by just providing a valid GitHub Token and the main GitHub repo. Once ROCCO has done all of its magic, you can `docker-compose up` a perfect replica of your odoo.sh project, submodules included. It can also be used the other way around, that is: to build a Docker Environments with an addons repo that will eventually build an odoo.sh project.

ROCCO is based on the standard [Odoo Docker images](https://hub.docker.com/_/odoo), and comes with Odoo Enterprise included by default. In case you don't want to use Odoo Enterprise, just comment out the corresponding line in the Dockerfile once you have built your docker-env. In the same way, feel free to customize the resulting template at your wish if you need to change its behaviour.

## Usage

Install [cookiecutter](http://cookiecutter.readthedocs.io/):
```bash
python3 -m pip install cookiecutter
```

Then run cookicutter passing it the directory containing this template
```bash
python3 -m cookiecutter .
```

You will be asked a few parameters, including the name and organization for both the addons repo and the docker-env repo. Then, the actual docker-env folder will be available for you. It will be automatically linked to the project addons repo you entered.

## Caveats
- A proxy server is not provided by the docker-compose orchestration.
- Accessing different submodules/repos with different github tokens (or with other mean of authentication) is not possible at the moment.
- Submodules are added to the odoo configuration addons_path in alphabetical order. This is meant to reproduce an undocumented feature of Odoo.sh
- The default odoo data directory is different from the one provided by the standard Odoo Docker Image. This is needed to prevent permission issues when the volume is re-declared in the composefile

## FIXME
- Submodules whose path inside the addons repo don't match their GitHub repo names are not properly handled. This will be fixed in a future release.
- Requirements from the submodules are not installed. This woo will be handled later on.

## Contributing
Pull requests are welcome. For major changes, please [open an issue](https://github.com/saydigital/rocco/issues) first to discuss what you would like to change. If your code is accepted in ROCCO, please proudly add your name to the Credits section here below.

## Credits
Thanks to [Francesco Apruzzese](https://github.com/opencode) for inventing the name of this long and durable piece of software.

ROCCO is based on ideas inspired by several different friend working at several different companies. Thank you all for sharing ideas, concepts, technologies and hints that brought to the creation of this tool.

Code and bugs made with ❤️ by [Andrea Colangelo](https://andreacolangelo.dev/).

## The boring stuff
Copyright 2021 © Andrea Colangelo <andrea.colangelo@rapsodoo.com> and Rapsodoo Italia SrL <https://www.rapsodoo.com/>.

ROCCO is free software, and is released under the terms of the [WTFPL](http://www.wtfpl.net/txt/copying/).

ROCCO is provided as is, without warranties of any kind. Use it at your own risk, and don't say you haven't been warned.
