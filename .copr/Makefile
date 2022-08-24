srpm:
	rpmbuild \
	--define "_disable_source_fetch 0" \
	--define "_sourcedir $(outdir)" \
	--define "_srcrpmdir $(outdir)" \
	-bs $(spec)
