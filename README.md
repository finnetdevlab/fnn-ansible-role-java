Ansbile Java Role
=========

Installs OpenJDK packages on Linux servers.

Requirements
------------

_None_

Role Variables
--------------

`java_package` variable defines generic version for OpenJDK. Default value of the variable is _default_.
 Default and available packages by platform can be found at [vars folder](./vars).

```yml
# Explicitly package definition format
java_package: <jre|jdk>-<java_version>
```
      


Dependencies
------------

_None_

Example Playbook
----------------

Install OpenJDK JDK 11. If you specify packages explicitly, ensure that your os distributions have
the required package version.

    - hosts: servers
      roles:
         - { role: fnn-ansible-role-java, java_package: jdk-11 }