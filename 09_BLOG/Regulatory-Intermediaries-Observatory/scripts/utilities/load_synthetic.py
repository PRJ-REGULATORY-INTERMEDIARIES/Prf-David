"""Local entrypoint; see README for environment setup."""
import sys
from rio.__main__ import main

if __name__ == "__main__":
    sys.argv.insert(1, 'load-synthetic')
    main()
