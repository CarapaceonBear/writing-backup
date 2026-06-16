## Writing Backup ##
---
This repository is a remote backup for my creative writing projects. I write in NovelWriter (https://novelwriter.io/), which saves files in plaintext, so it's easy to modify with code. 
I have put together some python scripts to encrypt and decrypt those text files (using a Vigenere cypher). I'm using very simple encryption, because my purpose is not to make my writing fully secure, 
I'm just protecting it against being scraped for AI training.
The encryption script makes a dated backup on my local machine before it does anything, and I have a script for manually restoring a backup from a specified date.
