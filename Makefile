.PHONY: all run clean zip

LOCAL: project_files/

all:
	# does nothing
run:
	python3 $(LOCAL)Bozo.py
clean:
	rm *.zip
zip:
	# Formatado para entrega no runcodes
	zip -r entrega.zip * -x "__pycache__/*" "README.md" ".gitignore"