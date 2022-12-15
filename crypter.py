import pyAesCrypt
import sys


def main():
	print('FastCrypter 1.0, by @valhallaProject')

	try:
		cmd = sys.argv[1]
	except IndexError:
		print('Please launch with command. Try "help" to view commands')
		sys.exit()

	if cmd == 'encrypt':
		try:
			file = sys.argv[2]
			pswd = sys.argv[3]
		except IndexError:
			print('Please launch with command. Try "help" to view commands')
			sys.exit()
		pyAesCrypt.encryptFile(file, f'{file}.encrypt', pswd)
	elif cmd == 'decrypt':
		try:
			file = str(sys.argv[2]).replace('.encrypt', '')
			pswd = sys.argv[3]
		except IndexError:
			print('Please launch with command. Try "help" to view commands')
			sys.exit()
		pyAesCrypt.decryptFile(f'{file}.encrypt', f'{file}.decrypt', pswd)
	elif cmd == 'help':
		print('encrypt [file] [password] - encrypt the file')
		print('decrypt [file] [password] - decrypt the file')
		print('help - view commands')
	else:
		print(f'Not found command "{cmd}". Try "help" to view commands.')


if __name__ == '__main__':
	main()