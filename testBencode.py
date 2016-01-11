import urllib
import hashlib
import bencode
import unittest

class TestToolBarOffer(unittest.TestCase):

    def setUp(self):
        global content
        url = "http://update.utorrent.com/installoffer.php?offer=conduit"
        content = urllib.urlopen(url).read()

    def test_ToolBarOffer(self):
        global content
        parsedResponse = bencode.bdecode(content)

        print parsedResponse
        binaryUrl = parsedResponse['offer_url']
        binaryHash = parsedResponse['offer_hash']
        
        binary_file = urllib.urlopen(binaryUrl).read()
        self.assertEqual(hashlib.sha1(binary_file), binaryHash)


if __name__ == "__main__":
    unittest.main()



