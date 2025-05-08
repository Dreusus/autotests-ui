def pytest_configure(config):
    if not hasattr(config, "workerinput"):
        config.stash["shared"] = {
            "key": "value"
        }


def pytest_configure_node(node):
    # это хук хдиста только.Вызывается на мастере на количество воркеров
    data = node.config.stash["shared"]
    node.workerinput["shared"] = data


def pytest_sessionstart(session):
    cfg = session.config
    if hasattr(cfg, "workerinput"):
        shared = cfg.workerinput["shared"]
        cfg.stash["shared"] = shared
