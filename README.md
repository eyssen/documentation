# 🛠️ eYssen Documentation (Odoo Community 18.0 Fork)

This repository contains the source files for the documentation of applications based on **Odoo Community**, maintained by **eYssen**.

This project is a fork of the **original** [odoo/documentation](https://github.com/odoo/documentation) repository's **18.0 branch**, which we have customized for the 18.0 Community release and eYssen-specific modules.

**License:** As this is a fork of the original Odoo documentation, it remains under the terms of the **CC-BY-SA-4.0** license.

---

## Build the documentation

The documentation is written in reStructuredText (`.rst`) format and can be generated into HTML using the Sphinx documentation generator.

### Requirements

- [Git](https://git-scm.com/install)
- [Python 3.10 to 3.14](https://www.python.org/downloads/).
- Make
- Python dependencies from the `requirements.txt` file (see instructions below)
- Local **eYssen application source** (a copy of your [eyssen/eyssen](https://github.com/eyssen/eyssen) repository) (optional – for including docstrings)
- Local copy of the [odoo/upgrade-util](https://github.com/odoo/upgrade-util) repository (optional)

### Quick start

1.  Create and activate a virtual environment.
    - For Linux and macOS: `python3 -m venv .venv && source .venv/bin/activate`
    - For Windows (PowerShell): `py3 -m venv .venv; .\.venv\Scripts\Activate.ps1`
2.  Install Python dependencies: `pip install -r requirements.txt`
3.  Build the documentation: `make html` (additional commands: `make help`)
4.  Open the `documentation/_build/html/index.html` file in your browser.

### Additional build options

* `make fast`: builds the documentation quickly with a shallow menu.
* `make clean`: deletes the build files.
* `make test`: runs tests for documentation directives.
* `make html CURRENT_LANG=fr`: builds the documentation only in French.
* `make html CURRENT_LANG=fr LANGUAGES=en,fr,de`: builds the documentation in French, enabling the language switcher.
* `make html CURRENT_LANG=hu`: builds the documentation only in Hungarian. When `CURRENT_LANG` is not `en`, `LANGUAGES` defaults to `en,<CURRENT_LANG>` so the language switcher shows both options.
* `make sitemap`: regenerates `_build/html/sitemap.xml` from the current HTML tree without rebuilding pages.

### Sitemap (`https://doc.eyssen.com/sitemap.xml`)

Each `make html` pass rebuilds a single site-wide sitemap at `_build/html/sitemap.xml`. The generator walks the published HTML tree (English at the root, Hungarian under `hu/`) and writes absolute URLs under `https://doc.eyssen.com/`. Sphinx utility pages (`search.html`, `genindex.html`), `_static` artifacts, and redirect stubs are omitted.

### robots.txt (`https://doc.eyssen.com/robots.txt`)

Sphinx copies `html_extra/robots.txt` to the HTML output root via `html_extra_path`.
It allows all crawlers and points at `https://doc.eyssen.com/sitemap.xml`.
Cloudflare may append content-signal comments at the edge; the origin file must
still contain `User-agent` / `Allow` / `Sitemap`.

### Canonical URLs

Production builds set `ROOT=https://doc.eyssen.com` and `IS_REMOTE_BUILD=True` by default (see `Makefile`). That makes `<link rel="canonical">` absolute under `https://doc.eyssen.com/…` via `conf.py` `_generate_alternate_urls` (same path the Odoo theme already supports). Empty `IS_REMOTE_BUILD=` restores relative canonicals for local preview. Alias hosts such as `doc.eyssen.uk` must 301 to `.com` at the edge (Traefik/Cloudflare) — that is outside this repo.

This is a post-build step (`scripts/generate_sitemap.py`) rather than `sphinx-sitemap`: languages are built in separate Makefile passes into different output directories, English is served without an `/en/` prefix, and `locale/` still contains unpublished languages. After `make html` then `make html CURRENT_LANG=hu`, the sitemap contains both `/` and `/hu/` URLs.

### Hungarian translation

To work on the Hungarian translation:

1.  Generate or update the translatable POT files: `make gettext`
2.  Initialize or update the Hungarian PO files: `python3 scripts/init_hu_locale.py`
3.  Edit the `.po` files in `locale/hu/LC_MESSAGES/` (e.g. with Poedit or a text editor)
4.  Build the Hungarian documentation: `make html CURRENT_LANG=hu`

> ℹ️ **Note on versions:** This repository focuses on the **Odoo 18.0** version. If you use version-switching related commands, make sure the `VERSIONS` parameter includes only the relevant versions, e.g. `VERSIONS=18.0`.

The list of available languages can be found in the `conf.py` file, in the `languages_names` variable.

If you build the documentation for a specific language, the build files will be created in the `documentation/_build/html/<language>/` folder.

### Using local eYssen/Odoo sources

If you have local clones for the **eYssen application source** (`eyssen/eyssen`) and/or `odoo/upgrade-util`, place them either:

-   as **siblings** to this repository (in the parent directory), **or**
-   inside the `documentation` directory.

If found in these locations, the build process will incorporate Python docstrings from these repositories, provided their version matches the documentation version.

### Troubleshooting

* **Language switcher is empty:** Ensure both languages are built. Run `make html` first (English), then `make html CURRENT_LANG=hu` (Hungarian). The switcher links will then work in both directions. The same two-pass build is what fills `sitemap.xml` with both languages.
* Check your Python version: `python3 --version` (should be 3.10–3.14)
* Make sure your virtual environment is active and dependencies are installed.
* If you have made changes to the file structure, try running `make clean` before building.
* If language or version switchers point to a missing file, check that you have built the documentation for all necessary languages and versions.
* The "Developer" documentation is only available in English.

---

## Contribute

Currently, this documentation is maintained according to **eYssen**'s own requirements. Any suggestions or content-related questions can be raised using the **[GitHub issue tracker](https://github.com/eyssen/documentation/issues)**.

If you wish to contribute to the content of the original Odoo documentation, please follow the [Introduction Guide](https://doc.eyssen.com/contributing/documentation.html) and use Odoo's official channels.