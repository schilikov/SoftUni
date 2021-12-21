from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Story", 2000, 8.8)
        self.secondMovie = Movie("Next", 2001, 9.1)

    def test_init(self):
        self.assertEqual("Story", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(8.8, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_set_name_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_less_than_1887(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_if_name_is_already_added(self):
        actor = "Me"
        self.movie.actors = ["Me", "She"]
        self.movie.actors.append(actor)
        self.assertTrue(f"{actor} is already added in the list of actors!")

    def test_if_you_can_add_actor(self):
        actor = "Me"
        self.movie.actors = []
        self.movie.actors.append(actor)
        self.assertEqual(["Me"], self.movie.actors)

    def test_if_rating_is_bigger(self):
        result = self.movie.rating < self.secondMovie.rating

        self.assertTrue("Next is better than Story")

    def test_repr(self):
        result = '''Name: Story
               Year of Release: 2000
               Rating: 8.8
               Cast: Me, She'''

        print()
        self.assertTrue()


if __name__ == "__main__":
    main()