import random
import sys
import argparse
import marshal
import lzma
import gzip
import bz2
import binascii
import zlib


def decode(source: str) -> str:
    if "lzma" in source:
        data = lzma.decompress(eval(source[53:-2]))
    elif "gzip" in source:
        data = gzip.decompress(eval(source[54:-2]))
    elif "bz2" in source:
        data = bz2.decompress(eval(source[51:-2]))
    elif "binascii" in source:
        data = binascii.a2b_base64(eval(source[69:-2])).decode()
    elif "zlib" in source:
        data = zlib.decompress(eval(source[51:-2]))
    else:
        print("Unable to identify compression mode used. Exiting..")
        sys.exit()
    return marshal.loads(data)


def main():
    parser = argparse.ArgumentParser(description='deobfuscate python programs'.title())
    parser.add_argument('-i', '--input', type=str, help='input file name'.title(), required=True)
    parser.add_argument('-o', '--output', type=str, help='output file name'.title(), required=True)
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        lines = f.readlines()
        obfuscate_line_num = -1
        for i, line in enumerate(lines):
            if "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(" in line:
                obfuscate_line_num = i
                break
        if obfuscate_line_num == -1:
            print("Could not find obfuscated code in the input file. Exiting..")
            sys.exit()
        obfuscate_code = lines[obfuscate_line_num][69:-2]

    deobfuscate_code = decode(obfuscate_code)

    with open(args.output, 'w') as f:
        f.write(deobfuscate_code)

    print(f"Deobfuscated code written to {args.output}")

def encode(source:str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, 'Py-Fuscate', 'exec'))
    if selected_mode is binascii:
        encoded = binascii.b2a_base64(marshal_encoded)
    else:
        encoded = selected_mode.compress(marshal_encoded)
    if selected_mode is binascii:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))'
        return TMP.format(encoded)
    else:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))'
        return TMP.format(selected_mode.__name__, encoded)

if __name__ == '__main__':
    main()
