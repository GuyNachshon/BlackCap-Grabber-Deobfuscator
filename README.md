# BlackCap-Grabber Deobfuscator
This is a Python script that can be used to deobfuscate Python programs obfuscated using the [BlackCap-Grabber](https://github.com/KSCHdsc/BlackCap-Grabber/) obfuscation tool. The deobfuscator can identify the compression mode used by the obfuscator, decompress the obfuscated code, and then unmarshal it to produce the original source code.

# Prerequisites
This script requires Python 3.x and the following standard libraries:

- argparse
- marshal
- lzma
- gzip
- bz2
- binascii
- zlib

# Usage
To use the script, run the following command:

```python deobfuscator.py -i input_file -o output_file```

where `input_file` is the name of the obfuscated Python program and `output_file` is the name of the file to write the deobfuscated code to.

# How it works
The deobfuscator reads the input file and searches for the obfuscated code. Once the obfuscated code is identified, the deobfuscator determines the compression mode used by the obfuscator and decompresses the obfuscated code accordingly. Finally, the deobfuscator unmarshals the decompressed code to produce the original source code and writes it to the output file.

# Limitations
This deobfuscator is specifically designed to work with Python programs obfuscated using the BlackCap-Grabber obfuscation tool. It may not work with other obfuscation tools or other obfuscation techniques. Also, note that this deobfuscator is not foolproof and may not be able to deobfuscate all programs obfuscated with BlackCap-Grabber.