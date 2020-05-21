Ansbile Java Role
=========

Installs OpenJDK packages on Linux servers.

Requirements
------------

_None_

Role Variables
--------------

`java_env` variable defines java environment for OpenJDK. Default value of the variable is 'jdk'.

```yml
# Environment definition can be 'jre' or 'jdk'
java_env: jdk
```

`java_ver` variable defines java version for OpenJDK. Default value of the variable is 'default'.

```yml
# Version definition for openJDK is platform dependent. Ensure that selected os distribution
# contains specified java version for their package manager.
# For oracleJDK available versions are 7, 8, 9, 10, 11.
java_ver: default
```

Dependencies
------------

_None_

Example Playbook
----------------

Install OpenJDK JRE 11. If you specify packages explicitly, ensure that your os distributions have
the required package version.

    - hosts: servers
      roles:
         - { role: fnn-ansible-role-java, java_env: jre, java_ver: 11 }