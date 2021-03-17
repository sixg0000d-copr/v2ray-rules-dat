srpm:
	rpmbuild \
	--undefine "_disable_source_fetch" \
	--define "_sourcedir $(outdir)" \
	--define "_srcrpmdir $(outdir)" \
	-bs $(spec)