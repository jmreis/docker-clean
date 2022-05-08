PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
MANDIR ?= $(PREFIX)/share/man/man1
DOCDIR ?= $(PREFIX)/share/doc/docker-clean

.PHONY: all install uninstall

all:

install:
	install -m755 -d $(DESTDIR)$(BINDIR)
	install -m755 -d $(DESTDIR)$(MANDIR)
	install -m755 -d $(DESTDIR)$(DOCDIR)
	gzip -c docker-clean.1 > docker-clean.1.gz
	install -m755 docker-clean $(DESTDIR)$(BINDIR)
	install -m644 docker-clean.1.gz $(DESTDIR)$(MANDIR)
	install -m644 README.md $(DESTDIR)$(DOCDIR)
	rm -f docker-clean.1.gz

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/docker-clean
	rm -f $(DESTDIR)$(MANDIR)/docker-clean.1.gz
	rm -rf $(DESTDIR)$(DOCDIR)

test:
	python3 docker-clean.py --help