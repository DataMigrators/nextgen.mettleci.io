# DevOps for DataStage

## Getting Started

### Install prerequisites.

Installing this handbook requires `python` and `pip` to be installed.

On MacOS you should need to install:

```
brew install cairo pango gdk-pixbuf libxml2 libxslt libffi python pandoc
```

### Install cookiecutter

You *may* need to install or upgrade cookiecutter:

```
python3 -m pip install --user --upgrade cookiecutter
```

### Run the repo locally

```
make serve
```

At this point you will be able to see your handbook, by browsing to [http://127.0.0.1:8000/datamigrators/nextgen.mettleci.io/](http://127.0.0.1:8000/datamigrators/nextgen.mettleci.io/).

### Push GitHub pages

```
make deploy
```

Note: For more help / targets, just type `make`

## Adding content:

1. Everything under the `/docs` folder becomes the website.
2. The table of contents (ToC) is created by https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin which means that that the structure is defined by the folders.
- Each folder has a `.pages` file which defines the names & other ToC definitions.
- For example, `docs/overview/index.md` will create a new section called Overview as the first section.
- You can change the name of the section by adding a `docs/overview/.pages` file. You can arrange pages with an `arrange` statement in the `.pages` file.

This makes editing simple - just add / edit content under `docs`, either by pushing the EDIT pencil button in the GitHub pages in your browser, or creating content via GitHub / git push. Everything will be built - including the updated ToC - automatically via GitHub actions. 

## Updating railroad diagrams in CLI documentation

Navigate to the `docs/railroads` folder and follow instructions in the [https://github.com/DataMigrators/nextgen.mettleci.io/tree/main/docs/railroads/README.md](README.md) file.


## Reviewing and providing feedback on the documents

- Please submit a *Pull request* with your suggested changes. This is highly encouraged, as it's the best way to contribute.
- Please open a [New Issue](https://github.com/DataMigrators/nextgen.mettleci.io/issues) if you have *general* feedback and comments.
