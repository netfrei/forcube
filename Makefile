all: alle

watch:
		watchmedo shell-command --patterns="*.pd" --command=pandoc

src = $(wildcard *.md)

paper.pdf: $(src)
	pandoc --toc -V colorlinks -H OpenScienceStyle.sty  -s author.yaml $(src) --highlight-style tango --filter pandoc-citeproc -F mermaid-filter -o $(basename $(src)).pdf --from markdown --template ./eisvogel.tex -N

word:
	pandoc -V colorlinks -H OpenScienceStyle.sty  -s author.yaml $(src) --highlight-style tango --filter pandoc-citeproc -F mermaid-filter -o $(basename $(src)).docx --from markdown --template ./eisvogel.tex -N

pandoc:
		pandoc authorNFDI.yaml --filter pandoc-citeproc -N -V colorlinks  -s --from markdown --template eisvogel.tex --top-level-division=chapter --highlight-style tango nfdi4sdout.pd -o nfdi4sd.tex

combine:
		mkdocscombine -o nfdi4sd.pd
		python nfdiFormatmd.py

alle:
	combine
	pandoc

clean:
	rm -rf tex2pdf*
