# simple-vernam-cipher
Simple functions to implement Vernam cipher.

The Vernam cipher is a substitution cipher where each plain text character is encrypted using its own key. 
This key — or key stream — is randomly generated or is taken from a one-time pad, e.g. a page of a book. 
The key must be equal in length to the plain text message. The fact that each character of the message is encrypted 
using a different key prevents any useful information being revealed through a frequency analysis of the cipher text.

To encrypt the message, each character of the plain text and the key will need to be converted to a numeric code. 
In the ASCII coding system, each character is given a numeric code. For example, the letter `'H'` is `72`. 
This number has a binary representation of `01001000` (using 8 bits).

To apply the Vernam cipher, each bit of the binary character code for each letter of the plain text undergoes a 
`XOR` operation with the corresponding bit of each letter of the binary character code for the corresponding 
character from the key stream — this creates the cipher text.

### Usage exaple

```
print(vernam_encrypt('DOG', 'CAT'))
print(vernam_decrypt([24, 9, 25, 24, 0], 'PLUTO')
```
#### Output:

```
[7, 14, 19]
HELLO
```
