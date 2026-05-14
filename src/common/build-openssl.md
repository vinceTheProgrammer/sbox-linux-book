# Build openssl 3.0.13

1. Download the source archive:
```sh
curl -LO https://github.com/openssl/openssl/releases/download/openssl-3.0.13/openssl-3.0.13.tar.gz
```

2. Extract it:
```sh
tar xf openssl-3.0.13.tar.gz
```

3. Navigate into extracted source directory:
```sh
cd openssl-3.0.13
```

4. Build as per the included `INSTALL.md`. For convenience, the prerequisites and commands found in `openssl-3.0.13/INSTALL.md` are mirrored here:
```
Prerequisites
=============
 * A "make" implementation
 * Perl 5 with core modules (please read [NOTES-PERL.md](NOTES-PERL.md))
 * The Perl module `Text::Template` (please read [NOTES-PERL.md](NOTES-PERL.md))
 * an ANSI C compiler
 * a development environment in the form of development libraries and C
   header files
 * a supported operating system
```
```sh
./Configure
make
make test
```

`libssl.so.3` and `libcrypto.so.3` should now be located at the root of the extracted source directory. i.e. `openssl-3.0.13/libssl.so.3` and `openssl-3.0.13/libcrypto.so.3`