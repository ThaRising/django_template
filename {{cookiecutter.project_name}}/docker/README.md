# Docker

This short guide describes
how to use the included
Docker configuration.

## Adding new Services

When adding a new service,
be sure to add the base configuration
to the ``docker-compose.yml``
file.

All volumes should be included
in the ``docker-compose.vols.yml``,
**NOT** in the main file.

Any deviating configurations
or volumes for testing purposes
should be added to the
``docker-compose.test.yml`` file.  
Keep in mind that this file may
also contain volumes, that serve
only for a single test-run.
