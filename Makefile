SRC	:= notetaker.py
VENDOR	:= v/lib/python3.6/site-packages
FILES	:= $(SRC) $(VENDOR)

DEST	:= notetaker.zip

.PHONY: all
all: $(DEST)

$(DEST): $(SRC)
	./zip.sh -FSro $(DEST) $(SRC) $(VENDOR)

.PHONY: upload
upload: $(DEST)
	aws lambda update-function-code \
		--function-name $(NOTETAKER_LAMBDA_FUNCTION) \
		--zip-file fileb://$(DEST)
