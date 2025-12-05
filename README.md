# 🛠️ eYssen Dokumentáció (Odoo Community 18.0 Fork)

Ez a tároló az **eYssen** által fenntartott, **Odoo Community** alapú alkalmazásokhoz készült dokumentáció forrásfájljait tartalmazza.

Ez a projekt az **eredeti** [odoo/documentation](https://github.com/odoo/documentation) tároló **18.0-ás ágának** (branch) forkja, amelyet a 18.0-ás Community kiadáshoz és az eYssen specifikus modulokhoz szabtunk.

**Licenc:** Mivel ez az eredeti Odoo dokumentáció forkja, továbbra is a **CC-BY-SA-4.0** licenc feltételei vonatkoznak rá.

---

## Dokumentáció Építése (Build the documentation)

A dokumentáció reStructuredText (`.rst`) formátumban íródott, és a Sphinx dokumentáció-generátor segítségével állítható elő HTML formátumban.

### Előfeltételek (Requirements)

- [Git](https://git-scm.com/install)
- [Python 3.10 to 3.14](https://www.python.org/downloads/).
- Make
- Python függőségek a `requirements.txt` fájlból (lásd az alábbi utasításokat)
- A helyi **eYssen alkalmazás forrása** (az Ön [eyssen/eyssen](https://github.com/eyssen/eyssen) tárolójának másolata) (opcionális – a docstringek bevonásához)
- A helyi [odoo/upgrade-util](https://github.com/odoo/upgrade-util) tároló másolata (opcionális)

### Gyors Indítás (Quick start)

1.  Hozzon létre és aktiváljon egy virtuális környezetet.
    - Linux és macOS esetén: `python3 -m venv .venv && source .venv/bin/activate`
    - Windows esetén (PowerShell): `py3 -m venv .venv; .\.venv\Scripts\Activate.ps1`
2.  Telepítse a Python függőségeket: `pip install -r requirements.txt`
3.  Építse fel a dokumentációt: `make html` (további parancsok: `make help`)
4.  Nyissa meg a `documentation/_build/html/index.html` fájlt a böngészőjében.

### További Építési Opciók (Additional build options)

* `make fast`: a dokumentáció gyors felépítése sekély menüvel.
* `make clean`: a build fájlok törlése.
* `make test`: a dokumentációs irányelvek tesztjeinek futtatása.
* `make html CURRENT_LANG=fr`: a dokumentáció felépítése csak francia nyelven.
* `make html CURRENT_LANG=fr LANGUAGES=en,fr,de`: a dokumentáció felépítése francia nyelven, engedélyezve a nyelvi váltót.

> ℹ️ **Megjegyzés a verziókról:** Ez a tároló az **Odoo 18.0** verzióra összpontosít. Amennyiben a verzióváltóval kapcsolatos parancsokat használja, győződjön meg róla, hogy a `VERSIONS` paraméter csak a releváns verziókat tartalmazza, pl. `VERSIONS=18.0`.

A rendelkezésre álló nyelvek listája a `conf.py` fájlban, a `languages_names` változóban található.

Ha a dokumentációt egy adott nyelvre építi, a build fájlok a `documentation/_build/html/<language>/` mappában jönnek létre.

### Helyi eYssen/Odoo Források Használata (Using local eYssen/Odoo sources)

Ha rendelkezik helyi klónokkal az **eYssen alkalmazás forrásához** (`eyssen/eyssen`) és/vagy az `odoo/upgrade-util`-hoz, helyezze el azokat:

-   ennek a tárolónak a **testvéreként** (a szülőkönyvtárban), **vagy**
-   a `documentation` könyvtáron belül.

Ha ezeken a helyeken megtalálhatóak, a build folyamat bevonja a Python docstringeket ezekből a tárolókból, amennyiben a verziójuk megegyezik a dokumentáció verziójával.

### Hibaelhárítás (Troubleshooting)

* Ellenőrizze a Python verzióját: `python3 --version` (3.10–3.14 kell legyen)
* Győződjön meg róla, hogy a virtuális környezet aktív, és a függőségek telepítve vannak.
* Ha változtatásokat eszközölt a fájlstruktúrában, próbálja meg a `make clean` parancsot a build előtt.
* Ha a nyelv- vagy verzióváltók hiányzó fájlra irányítanak, ellenőrizze, hogy az összes szükséges nyelvre és verzióra felépítette-e a dokumentációt.
* A "Developer" dokumentáció csak angol nyelven érhető el.

---

## Hozzájárulás (Contribute)

Jelenleg ez a dokumentáció az **eYssen** saját igényei szerint van karbantartva. Bármilyen javaslatot vagy tartalommal kapcsolatos kérdést feltehet a **[GitHub issue tracker](https://github.com/eyssen/documentation/issues)** segítségével.

Ha az eredeti Odoo dokumentáció tartalmához szeretne hozzájárulni, kérjük, kövesse az [Introduction Guide](https://www.odoo.com/documentation/latest/contributing/documentation.html) útmutatásait és használja az Odoo hivatalos csatornáit.