import testinfra.utils.ansible_runner
import pytest
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/node-exporter/",
])
def test_directories_creation(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("service", [
    "node-exporter"
])
def test_service_is_running(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("port", [
    "9100"
])
def test_socket(host, port):
    s = host.socket("tcp://127.0.0.1:{}".format(port))
    assert s.is_listening
