.PHONY: all run clean zip

LOCAL = project_files/

all:
	# does nothing

run:
	python3 $(LOCAL)__main__.py

clean:
	rm -f *.zip

zip:
	cd project_files && zip -r ../entrega.zip * -x "*__pycache__*"