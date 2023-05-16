from pytube_dlr import app

INVALID_UI = ['bsd_cli', 'win_cli']


def test_setup():
    for ui in INVALID_UI:
        try:
            app.setup(ui)
            raise BaseException(f'the function app.setup() accepts {ui}')

        except Exception as err:
            assert type(err) in (ValueError, KeyError)
