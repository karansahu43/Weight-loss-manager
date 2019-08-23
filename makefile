clean:
	rm -rf *.txt
debug:
	python3 The\ Weight\ Manager.py

optimize:
	git add makefile
	git commit -m "modified makefile"
	git push