FROM texlive/texlive:latest

COPY requirements.txt /build/
WORKDIR /build

RUN apt-get update &&\
    apt-get install -y python3 python3-pip python3-dev graphviz libgraphviz-dev pkg-config &&\
    pip install -r requirements.txt --break-system-packages

COPY dummy /dummy
COPY entrypoint.sh /build/entrypoint.sh
RUN chmod a+x /build/entrypoint.sh
WORKDIR /dummy
ENTRYPOINT ["/build/entrypoint.sh"]
