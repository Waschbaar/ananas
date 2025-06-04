# Playground for analytic stacks project

This repo contains the technical tools to help build a website.
Leanblueprint is a pretty handy tool that we use.
But we have no plan for formalizing the content.

## Compile

First, build the docker container:
```
docker build -t ananas:1 container
```
Then the project can be compiled by
```
docker run --rm -it -v ./:/dummy/blueprint/src -w /dummy ananas:1
```
The compiled website can be served by
```
docker run --rm -it -p 8082:80 -v ./build/web:/usr/share/nginx/html:ro nginx
```
which will be accesible at
[http://localhost:8082/](http://localhost:8082/).
In addition a pdf file will be in the `build` directory.
Plastex doesn't invoke bibtex automatically so it is necessary (?) to compile a pdf version frist.
Compilation will create `web.bbl` and `web.paux` in the source code tree.
They're in `.gitignore` so shouldn't a problem.
