import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts('all')

def test_if_java_installed(host):
    cmd = host.run("java -version")
    assert cmd.rc == 0

def test_if_JAVA_HOME_present(host):
    cmd = host.run("echo $JAVA_HOME")
    assert cmd.stdout