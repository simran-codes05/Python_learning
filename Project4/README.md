-- Caesar Cipher – Encryption & Decryption
-- Project Description

This is a simple Caesar Cipher Encryption and Decryption Program developed using Python.

The Caesar Cipher is one of the oldest encryption techniques. It works by shifting each letter of a message by a fixed number of positions in the alphabet.

This program allows users to:

Encrypt a message using a shift number.
Decrypt an encrypted message using the same shift number.
Preserve spaces, numbers, and special characters.
Choose between encryption and decryption.
Perform multiple encryption or decryption operations without restarting the program.

-- Features
Encryption: Converts plain text into encrypted text.
Decryption: Converts encrypted text back into plain text.
Custom Shift: Users can enter their own shift number.
Uppercase and Lowercase Support: Handles both uppercase and lowercase alphabets.
Special Character Support: Spaces, numbers, and symbols remain unchanged.
Multiple Operations: Allows users to encrypt or decrypt multiple messages in one session.
Loop Functionality: The program continues until the user chooses to exit.

-- Example Output
Encryption
text
Type encrypt for encrypt, Type decrypt for decrypt: encrypt

Type your message: hello

Type shift number: 3

Here your encrypt text: khoor

Type 'yes' if you want to go again other wise type 'no': yes

Decryption
text
Type encrypt for encrypt, Type decrypt for decrypt: decrypt

Type your message: khoor

Type shift number: 3

Here your decrypt text: hello

Type 'yes' if you want to go again other wise type 'no': no

Bye

-- Encryption Formula:

python
new_position = (position + shift_number) % 26

Decryption Formula:

python
new_position = (position - shift_number) % 26

-- Future Improvements 

Add input validation for shift numbers.
Allow users to enter uppercase and lowercase messages without converting everything to lowercase.
Improve the code by using the string module.
Add a graphical user interface (GUI).
Add support for more encryption techniques.

-- Developed as a beginner-friendly Python project to practice:

Functions
Lists
Loops
Conditional statements
String manipulation
User input
Mathematical operations
