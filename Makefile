BASE = django_doctest
DEST = django_doctest_${REL}
release:
	@rm -rf ${DEST}
	@mkdir ${BASE}/${DEST}
	@cp django_doctest_tests/src/django_doctest.py ${BASE}/${DEST}
	@cd ${BASE}; zip -q -r ${DEST}.zip ${DEST}; openssl sha1 ${DEST}.zip >>sha1sum; cat sha1sum
	@rm -rf ${BASE}/${DEST}
clean:
	@find ../ -name "*.pyc" -delete
test:
	@cd django_doctest_tests; ./manage.py test

