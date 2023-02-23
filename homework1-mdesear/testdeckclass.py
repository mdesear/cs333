import deck, unittest

class TestDeckClass(unittest.TestCase):
    def test_deal(self):
        testDeck = deck.Deck()
        testCard = testDeck.deal()

        self.assertEqual(testDeck.graveyard[0].suit, testCard.suit)
        self.assertEqual(testDeck.graveyard[0].rank, testCard.rank)
        
    def test_shuffle(self):
        testDeck = deck.Deck()

        shuffledDeck = testDeck.shuffle()

        self.assertNotEqual(testDeck, shuffledDeck)
        
    def test_reshuffle(self):
        testDeck = deck.Deck()
        testGraveyard = [None] * 52
        numCards = 0
        
        while numCards < 52:
            testGraveyard[numCards] = testDeck.deal()
            numCards += 1
        
        self.assertNotEqual(testDeck.deal(), None)
        
if __name__ == "__main__":
    unittest.main()