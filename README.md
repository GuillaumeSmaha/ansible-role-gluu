Deprecated
=========

**Note: This project is deprecated**


This role was splitted into mutiple roles:

- https://github.com/GuillaumeSmaha/ansible-role-gluu-cluster-manager
- https://github.com/GuillaumeSmaha/ansible-role-gluu-setup
- https://github.com/GuillaumeSmaha/ansible-role-gluu-configuration
- https://github.com/GuillaumeSmaha/ansible-role-gluu-customization

You can find playbook examples at:
- https://github.com/GuillaumeSmaha/ansible-gluu-playbook

Gluu
=========


Installs and update gluu on RedHat/CentOS or Debian/Ubuntu linux servers.

This role installs and configures the latest/selected version of gluu from the Gluu yum repository (on RedHat-based systems) or via apt (on Debian-based systems).


Requirements
------------

None.

Role Variables
--------------

`gluu_version:`
Define a custom version of the package to install.
To get a list of available package versions visit: https://gluu.org/docs/ce/

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: server
  roles:
    - role: gluu
  vars:
    gluu_version: 3.0.1 # (default is 3.0.2)
```

License
-------

LGPL-3.0

Author Information
------------------

Guillaume Smaha
