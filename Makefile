# Makefile for Sphinx documentation

# Pass WORKERS=1 for single-worker build
ifndef WORKERS
  WORKERS = auto
endif

ifndef BUILD_DIR
  BUILD_DIR    = _build
endif

ifndef CURRENT_LANG
  CURRENT_LANG = en
endif

# Default LANGUAGES for the language switcher (always include en and hu)
ifndef LANGUAGES
  LANGUAGES = en,hu
endif

# Absolute canonical host for production HTML. Relative canonicals (the previous
# default when ROOT/IS_REMOTE_BUILD were empty) let Google pick doc.eyssen.uk as
# googleCanonical while both hosts return 200. Override with IS_REMOTE_BUILD=
# (empty) for local file:// browsing.
ifndef ROOT
  ROOT = https://doc.eyssen.com
endif
ifndef IS_REMOTE_BUILD
  IS_REMOTE_BUILD = True
endif

SPHINX_BUILD   = sphinx-build
CONFIG_DIR     = .
SPHINXOPTS     = -D project_root=$(ROOT) -D canonical_version=$(CANONICAL_VERSION) \
                 -D versions=$(VERSIONS) -D languages=$(LANGUAGES) -D language=$(CURRENT_LANG) \
                 -D is_remote_build=$(IS_REMOTE_BUILD) \
                 -T \
                 -A plausible_script=$(PLAUSIBLE_SCRIPT) \
                 -A plausible_domain=$(PLAUSIBLE_DOMAIN) \
				 -j $(WORKERS)
# Override conf.py html_context only when the env/Make var is set. Passing
# -A google_analytics_key= with an empty value would wipe the default ID.
ifdef GOOGLE_ANALYTICS_KEY
  SPHINXOPTS += -A google_analytics_key=$(GOOGLE_ANALYTICS_KEY)
endif
SOURCE_DIR     = content

HTML_BUILD_DIR = $(BUILD_DIR)/html
ifdef VERSIONS
  HTML_BUILD_DIR := $(HTML_BUILD_DIR)/18.0
endif
ifneq ($(CURRENT_LANG),en)
  HTML_BUILD_DIR := $(HTML_BUILD_DIR)/$(CURRENT_LANG)
endif

#=== Standard rules ===#

.PHONY: all help clean html latexpdf gettext fast static test review sitemap robots

# In first position to build the documentation from scratch by default
all: html

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  html         to build the documentation to HTML"
	@echo "  fast         to build the documentation to HTML with shallow menu (faster)"
	@echo "  sitemap      to regenerate _build/html/sitemap.xml from the current HTML tree"
	@echo "  robots       to copy html_extra/robots.txt into the HTML output root"
	@echo "  clean        to delete the build files"
	@echo "  test         to run the guidelines tests"

clean:
	@echo "Cleaning build files..."
	rm -rf $(BUILD_DIR)/*
	@echo "Cleaning finished."

html: $(HTML_BUILD_DIR)/_static/style.css compile-mo
	@echo "Starting build..."
	$(SPHINX_BUILD) -c $(CONFIG_DIR) -b html $(SPHINXOPTS) $(SOURCE_DIR) $(HTML_BUILD_DIR)
	@$(MAKE) --no-print-directory sitemap
	@$(MAKE) --no-print-directory robots
	@echo "Build finished."

# Rebuild the site-wide sitemap from whatever HTML is already on disk.
# English lives at $(BUILD_DIR)/html/; Hungarian at $(BUILD_DIR)/html/hu/.
# Running this after each language pass keeps https://doc.eyssen.com/sitemap.xml
# in sync with both trees.
sitemap:
	@echo "Generating sitemap..."
	python3 scripts/generate_sitemap.py $(BUILD_DIR)/html
	@echo "Sitemap written to $(BUILD_DIR)/html/sitemap.xml"

# Ensure /robots.txt is present at the HTML root even for --apply without rebuild.
# Sphinx also copies this via html_extra_path during `make html`.
robots:
	@echo "Installing robots.txt..."
	cp html_extra/robots.txt $(BUILD_DIR)/html/robots.txt
	@echo "robots.txt written to $(BUILD_DIR)/html/robots.txt"

compile-mo:
	@find locale -name "*.po" | while read po; do \
		mo="$${po%.po}.mo"; \
		msgfmt -o "$$mo" "$$po"; \
	done

# To call *after* `make html`
# Binary dependencies (Debian): texlive-fonts-recommended texlive-latex-extra
# texlive-fonts-extra
latexpdf:
	@echo "Starting build..."
	$(SPHINX_BUILD) -c $(CONFIG_DIR) -b latex $(SPHINXOPTS) $(SOURCE_DIR) $(BUILD_DIR)/latex
	$(MAKE) -C $(BUILD_DIR)/latex
	cp $(BUILD_DIR)/latex/*.pdf $(BUILD_DIR)/html/
	@echo "Build finished."

gettext:
	@echo "Generating translatable files..."
	$(SPHINX_BUILD) -c $(CONFIG_DIR) -b gettext $(SOURCE_DIR) locale/sources
	@echo "Generation finished."

$(HTML_BUILD_DIR)/_static/style.css: extensions/odoo_theme/static/style.scss extensions/odoo_theme/static/scss/*.scss
	@echo "Compiling stylesheets..."
	mkdir -p $(HTML_BUILD_DIR)/_static
	python3 -m pysassc extensions/odoo_theme/static/style.scss $(HTML_BUILD_DIR)/_static/style.css
	@echo "Compilation finished."

#=== Development and debugging rules ===#

fast: SPHINXOPTS += -A collapse_menu=True
fast: html

static: $(HTML_BUILD_DIR)/_static/style.css
	cp -r extensions/odoo_theme/static/* $(HTML_BUILD_DIR)/_static/
	cp -r static/* $(HTML_BUILD_DIR)/_static/

# Called by runbot for the ci/documentation_guideline check.
test:
	@python tests/main.py $(SOURCE_DIR)/administration $(SOURCE_DIR)/applications $(SOURCE_DIR)/contributing $(SOURCE_DIR)/developer redirects

# Similar to `test`, but called only manually by content reviewers to specify a path and a max line
# length.
review:
	@read -p "Enter relative content path: " path; read -p "Enter max line length (default: 100): " line_length; \
	if [ -z "$$path" ]; then echo "Error: Path cannot be empty"; exit 1; fi; \
	if echo $$path | grep -q 'content/'; then path=`echo $$path | sed 's|content/||'`; fi; \
	if [ -z "$$line_length" ]; then line_length=100; fi; \
	export REVIEW=1; \
	python tests/main.py --max-line-length=$$line_length $(SOURCE_DIR)/$$path
