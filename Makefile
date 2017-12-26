SRC	:= notetaker.py
DEST	:= notetaker.zip

.PHONY: all
all: $(DEST)

$(DEST): $(SRC)
	./zip.sh -FSro $(DEST) $(SRC)

.PHONY: upload
upload: $(DEST)
	aws lambda update-function-code \
		--function-name $(NOTETAKER_LAMBDA_FUNCTION) \
		--zip-file fileb://$(DEST)
