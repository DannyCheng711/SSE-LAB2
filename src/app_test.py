from app import process_query


def test_knows_about_dinosaurs():
    # if condition returns True, then nothing happens
    # #if condition returns False, AssertionError is raised
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
    assert process_query("Which of the following numbers is the largest: 96, 93, 37?") == "96"
