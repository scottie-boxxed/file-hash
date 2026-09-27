# language: Python 3, file: hash.py
import hashlib
import sys
import argparse


def hash_file(path, algo="sha256", chunk=65536):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while True:
            block = f.read(chunk)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-a", "--algo", default="sha256", choices=["sha256", "md5", "sha1"])
    parser.add_argument("--verify")
    args = parser.parse_args()
    digest = hash_file(args.path, args.algo)
    print(f"{args.algo}: {digest}")
    if args.verify:
        ok = digest.lower() == args.verify.lower()
        print("MATCH" if ok else "MISMATCH")
        sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
