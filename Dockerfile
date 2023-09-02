FROM pypy:latest
RUN pip3 install spacy==${SPACY_VERSION}
RUN python3 -m spacy.${LANG}.download all
WORKDIR /app
COPY . /app
CMD python watch_next.py