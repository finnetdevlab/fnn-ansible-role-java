import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_if_java_installed(host):
    cmd = host.run('java -version')
    assert cmd.succeeded


def test_if_JAVA_HOME_present(host):
    assert host.file('/etc/profile').contains('JAVA_HOME')


def test_if_JAVA_HOME_defined_correctly(host):
    content = host.file('/etc/profile').content_string
    matched = [line for line in content.split('\n') if 'JAVA_HOME' in line]
    java_home = matched[0].split('=')[1]
    if host.run(java_home + '/jre/bin/java -version').succeeded or \
            host.run(java_home + '/bin/java -version').succeeded:
        assert True
    else:
        assert False
