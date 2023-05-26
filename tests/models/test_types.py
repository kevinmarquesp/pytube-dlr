from pytube_dlr.models.types import InfoYoutubeVideo


def test_InfoYoutubeVideo():
    tmpl_title: str = 'Rick Astley - Never Gonna Give You Up (Official Music Video)'
    tmpl_url: str = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    tmpl_err: str = 'watch?v=dQw4w9WgXcQ'

    normal_video: InfoYoutubeVideo = InfoYoutubeVideo(title=tmpl_title, url=tmpl_url)

    assert normal_video.title == tmpl_title
    assert normal_video.url == tmpl_url

    try:
        err_video: InfoYoutubeVideo = InfoYoutubeVideo(title=tmpl_title, url=tmpl_err)
        assert err_video.title == tmpl_title

    except Exception as err:
        assert type(err) is ValueError
