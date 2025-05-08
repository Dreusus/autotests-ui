import pytest


@pytest.fixture(scope="session")
def shared(request):
    print("[FIXTURE] stash =", request.config.stash["shared"])
    return request.config.stash["shared"]
