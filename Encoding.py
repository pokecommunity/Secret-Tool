#!/usr/local/bin/python
# -*- coding: utf-8 -*-

ENCODING = [
("\\x00",' '),
("\\x01",'À'),("\\x01",'\xC0'),
("\\x02",'Á'),("\\x02",'\xC1'),
("\\x03",'Â'),("\\x03",'\xC2'),
("\\x04",'Ç'),("\\x04",'\xC7'),
("\\x05",'È'),("\\x05",'\xC8'),
("\\x06",'É'),("\\x06",'\xC9'),
("\\x07",'Ê'),("\\x07",'\xCA'),
("\\x08",'Ë'),("\\x08",'\xCB'),
("\\x09",'Ì'),("\\x09",'\xCE'),
("\\x0A",'[0A]'),
("\\x0B",'Î'),("\\x0B",'\xCD'),
("\\x0C",'Ï'),("\\x0B",'\xCF'),
("\\x0D",'Ò'),("\\x0D",'\xD2'),
("\\x0E",'Ó'),("\\x0E",'\xD3'),
("\\x0F",'Ô'),("\\x0F",'\xD4'),
("\\x10",'[OE]'),
("\\x11",'Ù'),("\\x11",'\xD9'),
("\\x12",'Ú'),("\\x12",'\xDA'),
("\\x13",'Û'),("\\x13",'\xDB'),
("\\x14",'Ñ'),("\\x14",'\xD1'),
("\\x15",'ß'),("\\x15",'\xDF'),
("\\x16",'à'),("\\x16",'\xE0'),
("\\x17",'á'),("\\x17",'\xE1'),
("\\x18",'[18]'),
("\\x19",'ç'),("\\x19",'\xE7'),
("\\x1A",'è'),("\\x1A",'\xE8'),
("\\x1B",'é'),("\\x1B",'\xE9'),
("\\x1C",'ê'),("\\x1C",'\xEA'),
("\\x1D",'ë'),("\\x1D",'\xEB'),
("\\x1E",'ì'),("\\x1E",'\xEC'),
("\\x1F",'[1F]'),
("\\x20",'î'),("\\x20",'\xEE'),
("\\x21",'ï'),("\\x21",'\xEF'),
("\\x22",'ò'),("\\x22",'\xF2'),
("\\x23",'ó'),("\\x23",'\xF3'),
("\\x24",'ô'),("\\x24",'\xF4'),
("\\x25",'[oe]'),
("\\x26",'ù'),("\\x26",'\xF9'),
("\\x27",'ú'),("\\x27",'\xFA'),
("\\x28",'û'),("\\x28",'\xFB'),
("\\x29",'ñ'),("\\x29",'\xF1'),
("\\x2A",'º'),("\\x2A",'\xB0'),
("\\x2B",'ª'),("\\x2B",'\xAA'),
("\\x2C",'¹'),("\\x2C",'\xB9'),
("\\x2D",'&'),("\\x2D",'\x26'),
("\\x2E",'+'),("\\x2E",'\x2B'),
("\\x2F",'[2F]'),
("\\x30",'[30]'),
("\\x31",'[31]'),
("\\x32",'[32]'),
("\\x33",'[33]'),
("\\x34",'[Lv]'),
("\\x35",'='),("\\x35",'\x3D'),
("\\x36",';'),("\\x36",'\x3B'),
("\\x37",'[37]'),
("\\x38",'[38]'),
("\\x39",'[39]'),
("\\x3A",'[3A]'),
("\\x3B",'[3B]'),
("\\x3C",'[3C]'),
("\\x3D",'[3D]'),
("\\x3E",'[3E]'),
("\\x3F",'[3F]'),
("\\x40",'[40]'),
("\\x41",'[41]'),
("\\x42",'[42]'),
("\\x43",'[43]'),
("\\x44",'[44]'),
("\\x45",'[45]'),
("\\x46",'[46]'),
("\\x47",'[47]'),
("\\x48",'[48]'),
("\\x49",'[49]'),
("\\x4A",'[4A]'),
("\\x4B",'[4B]'),
("\\x4C",'[4C]'),
("\\x4D",'[4D]'),
("\\x4E",'[4E]'),
("\\x4F",'[4F]'),
("\\x50",'[50]'),
("\\x51",'¿'),("\\x51",'\xBF'),
("\\x52",'¡'),("\\x52",'\xA1'),
("\\x53",'[PK]'),
("\\x54",'[MN]'),
("\\x55",'[PO]'),
("\\x56",'[Ké]'),("\\x56",'[K\xE9]'),
("\\x57",'[BL]'),
("\\x58",'[OC]'),
("\\x59",'[K]'),
("\\x5A",'Í'),("\\x5A",'\xCD'),
("\\x5B",'%'),("\\x5B",'\x25'),
("\\x5C",'('),("\\x5C",'\x28'),
("\\x5D",')'),("\\x5D",'\x29'),
("\\x5E",'[5E]'),
("\\x5F",'[5F]'),
("\\x60",'[60]'),
("\\x61",'[61]'),
("\\x62",'[62]'),
("\\x63",'[63]'),
("\\x64",'[64]'),
("\\x65",'[65]'),
("\\x66",'[66]'),
("\\x67",'[67]'),
("\\x68",'â'),("\\x68",'\xE2'),
("\\x69",'[69]'),
("\\x6A",'[6A]'),
("\\x6B",'[6B]'),
("\\x6C",'[6C]'),
("\\x6D",'[6D]'),
("\\x6E",'[6E]'),
("\\x6F",'í'),("\\x6F",'\xED'),
("\\x70",'[70]'),
("\\x71",'[71]'),
("\\x72",'[72]'),
("\\x73",'[73]'),
("\\x74",'[74]'),
("\\x75",'[75]'),
("\\x76",'[76]'),
("\\x77",'[77]'),
("\\x78",'[78]'),
("\\x79",'[79]'),
("\\x7A",'[7A]'),
("\\x7B",'[7B]'),
("\\x7C",'[7C]'),
("\\x7D",'[7D]'),
("\\x7E",'[7E]'),
("\\x7F",'[7F]'),
("\\x80",'[80]'),
("\\x81",'[81]'),
("\\x82",'[82]'),
("\\x83",'[83]'),
("\\x84",'[84]'),
("\\x85",'[85]'),
("\\x86",'[86]'),
("\\x87",'[87]'),
("\\x88",'[88]'),
("\\x89",'[89]'),
("\\x8A",'[8A]'),
("\\x8B",'[8B]'),
("\\x8C",'[8C]'),
("\\x8D",'[8D]'),
("\\x8E",'[8E]'),
("\\x8F",'[8F]'),
("\\x90",'[90]'),
("\\x91",'[91]'),
("\\x92",'[92]'),
("\\x93",'[93]'),
("\\x94",'[94]'),
("\\x95",'[95]'),
("\\x96",'[96]'),
("\\x97",'[97]'),
("\\x98",'[98]'),
("\\x99",'[99]'),
("\\x9A",'[9A]'),
("\\x9B",'[9B]'),
("\\x9C",'[9C]'),
("\\x9D",'[9D]'),
("\\x9E",'[9E]'),
("\\x9F",'[9F]'),
("\\xA0",'[A0]'),
("\\xA1",'0'),
("\\xA2",'1'),
("\\xA3",'2'),
("\\xA4",'3'),
("\\xA5",'4'),
("\\xA6",'5'),
("\\xA7",'6'),
("\\xA8",'7'),
("\\xA9",'8'),
("\\xAA",'9'),
("\\xAB",'!'),("\\xAB",'\x21'),
("\\xAC",'?'),("\\xAC",'\x3F'),
("\\xAD",'.'),("\\xAD",'\x2E'),
("\\xAE",'-'),("\\xAE",'\x2D'),
("\\xAF",'|'),("\\xAF",'\x7C'),
("\\xB0",'[..]'),("\\xB0",'[\x2E\x2E]'),
("\\xB1",'["<]'),("\\xB1",'[\x22\x3C]'),
("\\xB2",'[>"]'),("\\xB2",'[\x3E\x22]'),
("\\xB3","'"),("\\xB3","\x27"),
("\\xB4",'\''),("\\xB4",'\x27'),
("\\xB5",'[MALE]'),("\\xB5",'[M]'),
("\\xB6",'[FEMALE]'),("\\xB6",'[F]'),
("\\xB7",'$'),("\\xB7",'\x24'),
("\\xB8",','),("\\xB8",'\x2C'),
("\\xB9",'×'),("\\xB9",'\xD7'),("\\xB9",'[B9]'),
("\\xBA",'/'),("\\xBA",'\x2F'),
("\\xBB",'A'),
("\\xBC",'B'),
("\\xBD",'C'),
("\\xBE",'D'),
("\\xBF",'E'),
("\\xC0",'F'),
("\\xC1",'G'),
("\\xC2",'H'),
("\\xC3",'I'),
("\\xC4",'J'),
("\\xC5",'K'),
("\\xC6",'L'),
("\\xC7",'M'),
("\\xC8",'N'),
("\\xC9",'O'),
("\\xCA",'P'),
("\\xCB",'Q'),
("\\xCC",'R'),
("\\xCD",'S'),
("\\xCE",'T'),
("\\xCF",'U'),
("\\xD0",'V'),
("\\xD1",'W'),
("\\xD2",'X'),
("\\xD3",'Y'),
("\\xD4",'Z'),
("\\xD5",'a'),
("\\xD6",'b'),
("\\xD7",'c'),
("\\xD8",'d'),
("\\xD9",'e'),
("\\xDA",'f'),
("\\xDB",'g'),
("\\xDC",'h'),
("\\xDD",'i'),
("\\xDE",'j'),
("\\xDF",'k'),
("\\xE0",'l'),
("\\xE1",'m'),
("\\xE2",'n'),
("\\xE3",'o'),
("\\xE4",'p'),
("\\xE5",'q'),
("\\xE6",'r'),
("\\xE7",'s'),
("\\xE8",'t'),
("\\xE9",'u'),
("\\xEA",'v'),
("\\xEB",'w'),
("\\xEC",'x'),
("\\xED",'y'),
("\\xEE",'z'),
("\\xEF",'[EF]'),
("\\xF0",':'),("\\xF0",'\x3A'),
("\\xF1",'Ä'),("\\xF1",'\xC4'),
("\\xF2",'Ö'),("\\xF2",'\xD6'),
("\\xF3",'Ü'),("\\xF3",'\xDC'),
("\\xF4",'ä'),("\\xF4",'\xE4'),
("\\xF5",'ö'),("\\xF5",'\xF6'),
("\\xF6",'ü'),("\\xF6",'\xFC'),
("\\xF7",'[F7]'),
("\\xF8",'[F8]'),
("\\xF9",'[F9]'),
("\\xFA",'[FA]'),
("\\xFB",'+'),("\\xFB",'\x2B'),
("\\xFC",'[FC]'),
("\\xFD",'[FD]'),
("\\xFE",'\n'),("\\xFE",'\x0A'),
]
