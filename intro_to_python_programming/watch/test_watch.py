from watch import parse


def test_valid_html_with_embed():
    assert (
        parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_invalid_html_no_embed():
    assert (
        parse('<iframe src="https://www.vimeo.com/embed/xvFZjo5PgG0"></iframe>') == None
    )
    assert parse('<iframe src="https://www.youtube.com/xvFZjo5PgG0"></iframe>') == None
    assert parse('<div src="https://www.youtube.com/embed/xvFZjo5PgG0"></div>') == None
    assert parse("<iframe></iframe>") == None
    assert parse("") == None


def test_edge_cases():
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0?autoplay=1"></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )
