#!/usr/bin/env python3


def Base64_Encodings_Tools(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	from pyfiglet import figlet_format
	from time import time, sleep
	import marshal
	import base64
	from datetime import datetime
	# Bersihkan layar
	system("clear")
	# Ubah izin file
	system("chmod 777 EncodingsToolsV2.py")
	tema=figlet_format("EncToolsV2",font="slant")
	print(tema)
	print("{!} Created By: Ruben Leonardo Sigalingging.")
	print("{!} Created On: Tuesday, 28 June 2022, 4:12 PM")
	print("{!} Function: Data Encoding Tool.\n")


	plaintext=str(input("{!} Enter Data To Encode: "))
	from base64 import b64encode
	enkode_ke_ASCII=plaintext.encode("ascii")
	ubah_ke_bit_base64=b64encode(enkode_ke_ASCII)
	dekode_ke_ASCII=ubah_ke_bit_base64.decode("ascii")
	print(f"[!] Encoding Results: {dekode_ke_ASCII}")
	print("\n")
# Base64_Encodings_Tools()


# Base16_Encodings_Tools
def Base16_Encodings_Tools(created_by="Ruben Leonardo Sigalingging."):
	from base64 import b16encode
	from os import system
	from pyfiglet import figlet_format
	system("clear")
	tema=figlet_format("EncToolsV2",font="slant")
	print(tema)
	print("{!} Created By: Ruben Leonardo Sigalingging.")
	print("{!} Created On: Tuesday, 28 June 2022, 4:12 PM")
	print("{!} Function: Data Encoding Tool.\n")


	plaintext=str(input("{!} Enter Data To Encode: "))
	enkode_ke_ASCII=plaintext.encode("ascii")
	ubah_ke_bit_base16=b16encode(enkode_ke_ASCII)
	dekode_ke_ASCII=ubah_ke_bit_base16.decode("ascii")
	print(f"[!] Encoding Results: {dekode_ke_ASCII}")
# Base16_Encodings_Tools()


# Base32
def Base32_Encodings_Tools(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	from pyfiglet import figlet_format
	from base64 import b32encode
	tema=figlet_format("EncToolsV2",font="slant")
	print(tema)
	print("{!} Created By: Ruben Leonardo Sigalingging.")
	print("{!} Created On: Tuesday, 28 June 2022, 4:12 PM")
	print("{!} Function: Data Encoding Tool.\n")


	plaintext=str(input("Enter Data To Encode: "))
	enkode_ke_ASCII=plaintext.encode("ascii")
	ubah_ke_bit_base32=b32encode(enkode_ke_ASCII)
	dekode_ke_ASCII=ubah_ke_bit_base32.decode("ascii")
	print(f"[!] Encoding Results: {dekode_ke_ASCII}")
# Base32_Encodings_Tools()


# Base85_Encodings_Tools
def Base85_Encodings_Tools(created_by="Ruben Leonardo Sigalingging."):
	from base64 import b85encode
	from os import system
	from pyfiglet import figlet_format
	tema=figlet_format("EncToolsV2",font="slant")
	print(tema)
	print("{!} Created By: Ruben Leonardo Sigalingging.")
	print("{!} Created On: Tuesday, 28 June 2022, 4:12 PM")
	print("{!} Function: Data Encoding Tool.\n")


	plaintext=str(input("Enter Data To Encode: "))
	enkode_ke_ASCII=plaintext.encode("ascii")
	ubah_ke_bit_base85=b85encode(enkode_ke_ASCII)
	dekode_ke_ASCII=ubah_ke_bit_base85.decode("ascii")
	print(f"[!] Encoding Results: {dekode_ke_ASCII}")
Base85_Encodings_Tools()


def Base85_Decodings_Tools():
	from base64 import b85decode
	from os import system
	from pyfiglet import figlet_format
	tema=figlet_format("DecToolsV2",font="slant")
	print(tema)
	print("{!} Created By: Ruben Leonardo Sigalingging.")
	print("{!} Created On: Tuesday, 28 June 2022, 4:12 PM")
	print("{!} Function: Data Encoding Tool.\n")


	Encrypted_Data=str(input("Enter Encrypted Data: "))
	enkode_ke_ASCII=Encrypted_Data.encode("ascii")
	ubah_ke_bit_base85=b85decode(enkode_ke_ASCII)
	dekode_ke_ASCII=ubah_ke_bit_base85.decode("ascii")
	print(f"[!] Decrypted Results: {dekode_ke_ASCII}")
Base85_Decodings_Tools()