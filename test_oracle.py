import oracle

def test_oracle_execution():
    """Ensure the oracle runs without raising exceptions"""
    try:
        oracle.speak("wisdom")
        oracle.speak("chaos")
        assert True
    except Exception as e:
        assert False, f"Oracle failed execution with error {e}"