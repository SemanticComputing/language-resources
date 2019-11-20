import unittest
from tokenization.FinnishTokenization import Tokenization

class TestTokenization(unittest.TestCase):
    def setUp(self):
        self.target = Tokenization()

    # test tokenization of a string to words and punctuation
    def test_word_tokenization(self):
        testset = ["Sauli aloitti kilpailut 1. ja 55. mm. kassalla ja hän on aina maalissa 8:ntena.",
                    "Myös Timo T. A. Mikkonen on työskennellyt mm. linja-auto tjms. kuskina USA:ssa.",
                    "Eduskuntaan A-, B- ja C-luokan ihmiset valitsivat Niinistön ensimmäisen kerran vuonna 1987.",
                    "Vapaa-aikanaan Timo T.A. Mikkonen mm. lentelee NH-90:llä -30°C:n pakkasessa!",
                    "Hänet valittiin uudelleen {tasavallan presidentiksi} 2018? Toinen kausi alkoi 1.2.2018.",
                    "Fahrenheit on termodynaaminen lämpötila-asteikko, jossa veden jäätymispiste on 32 astetta Fahrenheitia (°F) ja kiehumispiste 212 °F (normaalissa ilmanpaineessa).",
                    "Lämpötilaero 1 °F vastaa 0,556 °C lämpötilaeroa.",
                    "Mittayksikkö aine- ja tarviketiedoissa: Näissä tiedoissa on käytössä ainoastaan yksi mittayksikkö (ja yksi määrätieto) hyödykenimikettä kohden.",
                    "Tällöin on mielekkäämpää puhua esimerkiksi pikonewtoneista pN (1 pN=10-12 N).",
                    "Aikaisemmin (vuonna 1954) kelvin oli määritelty [lämpötilan] yksiköksi, joka oli 1/273,16 termodynaamisesta lämpötilasta veden kolmoispisteessä.",
                    " Vuonna 1971 vahvistettiin ensimmäinen SI-yksikköjärjestelmää käsittelevä suomalainen standardi (SFS 2300)",
                    "nykyisin SI-yksikköjärjestelmän perusstandardi (vrt. στιγμὴ τελεία) on maailmanlaajuinen (SFS-EN ISO 80000-1).",
                    "(vrt. στιγμὴ τελεία [2])", # TODO
                    """Bordeaux’ssa d'Artagnan ärähti: "Äitis oli!".""",
                    '"Tule mukaan!" hän pyysi.',
                    '”Ampui mies”, kirjoittaa Aleksis Kivi, ”ja kiirahtipa mesikämmen nurmelle nurin.”.',
                    "– Terve miestä, sinä Rajamäen Mikko! sanoi Juhani.– Kuinka jaksat ja mitä uutta maailmalta?",
                    "Läsnä: Makkonen, Matti; Laakso, Maija-Liisa; Lahtinen-Virtanen, Anna; Virtanen, Kalevi.",
                    "Ohjelmaa oli runsaasti: kiertoajelu kaupungin keskustassa; retkiä taide- ja kotimuseoihin; piknik omenatarhassa.",
                    "naimisissa/naimaton/leski/eronnut",
                    "Vedotaan §:ään 6!"
                    # HTML-tägit ?
                    ]
        expected_results =  [['Sauli', 'aloitti', 'kilpailut', '1.', 'ja', '55.', 'mm.', 'kassalla', 'ja', 'hän', 'on', 'aina', 'maalissa', '8:ntena', '.'],
                            ['Myös', 'Timo', 'T.', 'A.', 'Mikkonen', 'on', 'työskennellyt', 'mm.', 'linja-auto', 'tjms.', 'kuskina', 'USA:ssa', '.'],
                            ['Eduskuntaan', 'A', '-', ',', 'B', '-', 'ja', 'C-luokan', 'ihmiset', 'valitsivat', 'Niinistön', 'ensimmäisen', 'kerran', 'vuonna', '1987', '.'],
                            ['Vapaa-aikanaan', 'Timo', 'T.A.', 'Mikkonen', 'mm.', 'lentelee', 'NH-90:llä', '-30°C:n', 'pakkasessa', '!'],
                            ['Hänet', 'valittiin', 'uudelleen', '{', 'tasavallan', 'presidentiksi', '}', '2018', '?', 'Toinen', 'kausi', 'alkoi', '1.2.2018', '.'],
                            ['Fahrenheit', 'on', 'termodynaaminen', 'lämpötila-asteikko', ',', 'jossa', 'veden', 'jäätymispiste', 'on', '32', 'astetta', 'Fahrenheitia', '(', '°F', ')', 'ja', 'kiehumispiste', '212', '°F', '(', 'normaalissa', 'ilmanpaineessa', ')', '.'],
                            ['Lämpötilaero', '1', '°F', 'vastaa', '0,556', '°C', 'lämpötilaeroa', '.'],
                            ['Mittayksikkö', 'aine', '-', 'ja', 'tarviketiedoissa', ':', 'Näissä', 'tiedoissa', 'on', 'käytössä', 'ainoastaan', 'yksi', 'mittayksikkö', '(', 'ja', 'yksi', 'määrätieto', ')', 'hyödykenimikettä', 'kohden', '.'],
                            ['Tällöin', 'on', 'mielekkäämpää', 'puhua', 'esimerkiksi', 'pikonewtoneista', 'pN', '(', '1', 'pN=10-12', 'N', ')', '.'],
                            ['Aikaisemmin', '(', 'vuonna', '1954', ')', 'kelvin', 'oli', 'määritelty', '[', 'lämpötilan', ']', 'yksiköksi', ',', 'joka', 'oli', '1', '/', '273,16', 'termodynaamisesta', 'lämpötilasta', 'veden', 'kolmoispisteessä', '.'],
                            ['Vuonna', '1971', 'vahvistettiin', 'ensimmäinen', 'SI-yksikköjärjestelmää', 'käsittelevä', 'suomalainen', 'standardi', '(', 'SFS', '2300', ')'],
                            ['nykyisin', 'SI-yksikköjärjestelmän', 'perusstandardi', '(', 'vrt.', 'στιγμὴ', 'τελεία', ')', 'on', 'maailmanlaajuinen', '(', 'SFS-EN', 'ISO', '80000-1', ')', '.'],
                            ['(', 'vrt.', 'στιγμὴ', 'τελεία', '[', '2', ']', ')'],
                            ['Bordeaux’ssa', "d'Artagnan", 'ärähti', ':', '"', 'Äitis', 'oli', '!', '"', '.'],
                            ['"', 'Tule', 'mukaan', '!', '"', 'hän', 'pyysi', '.'],
                            ['”', 'Ampui', 'mies', '”', ',', 'kirjoittaa', 'Aleksis', 'Kivi', ',', '”', 'ja', 'kiirahtipa', 'mesikämmen', 'nurmelle', 'nurin.', '”', '.'],
                            ['–', 'Terve', 'miestä', ',', 'sinä', 'Rajamäen', 'Mikko', '!', 'sanoi', 'Juhani', '.', '–', 'Kuinka', 'jaksat', 'ja', 'mitä', 'uutta', 'maailmalta', '?'],
                            ['Läsnä', ':', 'Makkonen', ',', 'Matti', ';', 'Laakso', ',', 'Maija-Liisa', ';', 'Lahtinen-Virtanen', ',', 'Anna', ';', 'Virtanen', ',', 'Kalevi', '.'],
                            ['Ohjelmaa', 'oli', 'runsaasti', ':', 'kiertoajelu', 'kaupungin', 'keskustassa', ';', 'retkiä', 'taide', '-', 'ja', 'kotimuseoihin', ';', 'piknik', 'omenatarhassa', '.'],
                            ['naimisissa', '/', 'naimaton', '/', 'leski', '/', 'eronnut'],
                            ['Vedotaan', '§:ään', '6', '!']]

        for text, result in zip(testset, expected_results):
            self.assertEqual(self.target.word_tokenization(text), result)


if __name__ == '__main__':
    unittest.main()
