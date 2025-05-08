def test_example(shared):
    print(f"[TEST] shared_data: {shared}")
    assert "key" in shared

def test_shared(shared):
    assert shared == {"key": "value"}
