# node_exporter

Install, configure and maintain [node_exporter](https://github.com/prometheus/node_exporter)

## Role Philosophy

Please see
[ansible-consul](https://github.com/nahsi/ansible-consul#role-philosophy).

## Role Variables

See [defaults/](https://github.com/nahsi/ansible-node-exporter/blob/master/defaults/) for details and examples.

#### `node_exporter_version`

- version to use

#### `node_exporter_dirs`

- a map of directories to create
- default:

```yaml
node_exporter_dir: "/opt/node-exporter"
node_exporter_dirs:
  main:
    path: "{{ node_exporter_dir }}"
  certs:
    path: "{{ node_exporter_dir }}/certs"
  textfile:
    path: "{{ node_exporter_dir }}/textfile"
  logs:
    path: "/var/log/node-exporter"
```

#### `node_exporter_enabled_collectors`

- [collectors](https://github.com/prometheus/node_exporter#collectors)
- example: please see [defaults/example.yml](https://github.com/nahsi/ansible-node-exporter/blob/master/defaults/example.yml)
- default:
```yaml
node_exporter_enabled_collectors:
  - textfile:
      directory: "{{ node_exporter_dirs.textfile.path }}"
```

#### `node_exporter_disabled_collectors`

- [collectors](https://github.com/prometheus/node_exporter#collectors)
- example: please see [defaults/example.yml](https://github.com/nahsi/ansible-node-exporter/blob/master/defaults/example.yml)

#### `node_exporter_web_listen_address`

- default: `:9100`

#### `node_exporter_web_telemetry_path`

- default: `/metrics`

#### `node_exporter_user`

- owner of node_exporter process and files
- default: `node-exporter`

#### `node_exporter_group`

- group of `node_exporter_user`
- default: `node-exporter`

#### `node_exporter_service`

- openrc service file
- default: see [defaults/main.yml](https://github.com/nahsi/ansible-node-exporter/blob/master/defaults/main.yml)

#### `node_exporter_unitfile`

- systemd unit file
- default: see [defaults/main.yml](https://github.com/nahsi/ansible-node-exporter/blob/master/defaults/main.yml)

#### `skip_handlers`

- skip restart/reload - useful when building images with Packer
- default: `false`

## Tags

- `config` - update node-exporter unit/service and config file

## Author

- **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
