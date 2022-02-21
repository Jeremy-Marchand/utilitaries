from utilitaries.lib import try_me

def test_sum():
    phrase = try_me()
    assert 'Jérémy' in phrase.split()
