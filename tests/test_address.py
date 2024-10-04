from typing import Self
import unittest
from bitcoinaddress import Key, Address, Seed, address


class TestAddress(unittest.TestCase):

    def testFromWIF(self):
        # given
        key = Key.of('5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        address = Address.of(key)

        # then
        self.assertEqual(address.pubkey.upper(),
                         "04E61341F46B529B0FAC2C5E15A67AF7AFFCEB2BE7544AF18D14206FFF041C02C04D6CA36C97F458CFE5754CE15A8F32D4C917B5F0F5E336042EE3BE77C3F58222")
        self.assertEqual(address.pubkeyc.upper(), "02E61341F46B529B0FAC2C5E15A67AF7AFFCEB2BE7544AF18D14206FFF041C02C0")

        self.assertEqual(address.mainnet.pubaddr1, "1NaChZV4JJysct8QYcMKFHnQ2SNFpnBund")
        self.assertEqual(address.mainnet.pubaddr1c, "1D7XaU5PbsPxfZeYBcGGyMEqiVvPhtFMUF")

        self.assertEqual(len(address.pubkeyc), 66)

        self.assertEqual(len(address.mainnet.pubaddr1), 34)
        self.assertEqual(len(address.mainnet.pubaddr1c), 34)
        self.assertEqual(len(address.mainnet.pubaddr3), 34)
        self.assertEqual(len(address.mainnet.pubaddrbc1_P2WSH), 62)
        self.assertEqual(len(address.mainnet.pubaddrbc1_P2WPKH), 42)

        self.assertEqual(len(address.testnet.pubaddr1), 34)
        self.assertEqual(len(address.testnet.pubaddr1c), 34)
        self.assertEqual(len(address.testnet.pubaddr3), 35)
        self.assertEqual(len(address.testnet.pubaddrtb1_P2WSH), 62)
        self.assertEqual(len(address.testnet.pubaddr1_P2WPKH), 42)


if __name__ == "__main__":
    unittest.main()
