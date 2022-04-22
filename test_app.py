import pytest
from app import unique_characters


class TestClass:
    @pytest.mark.parametrize("s, result",
                             [
                                 ("abbabcde", 3),
                                 ("dkfppplllere", 4),
                                 ("ttppllffhgyyyy", 2),
                                 ("fhjkdppppprh", 5)
                             ]
                             )
    def test_unique_characters(self, s, result):
        assert unique_characters(s) == result

    def test_exceptions(self):
        with pytest.raises(TypeError):
            unique_characters("abcd")
            unique_characters(12345)

