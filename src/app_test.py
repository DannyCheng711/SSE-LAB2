from app import process_query


def test_knows_about_dinosaurs():
    # if condition returns True, then nothing happens
    # if condition returns False, AssertionError is raised
    assert (
        process_query("dinosaurs")
        == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_my_name():
    assert process_query("What is your name?") == "Computing genius"


def test_plus():
    assert process_query("What is 67 plus 86?") == "153"


def test_largest():
    assert (
        process_query(
            "Which of the following numbers is the largest: 96, 93, 37?"
        )
        == "96"
    )


def test_multiplied():
    assert process_query("What is 26 multiplied by 72?") == "1872"


def test_square_cube():
    assert (
        process_query(
            "Which of the following numbers is both a square and a cube: 4100, 3005, 2303, 9, 343, 64, 3345?"
        )
        == "64"
    )
