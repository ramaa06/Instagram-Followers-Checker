# Instagram Follow Checker

Un script en **Python** que compara tus listas de **seguidores** y **seguidos** de Instagram (archivos HTML exportados desde la app), y te muestra qué personas **vos seguís pero no te siguen**.

---

## Cómo funciona

Instagram te permite descargar tu información desde el *Centro de cuentas*.  
Este script usa esos archivos para analizar las diferencias entre:

- `followers_1.html` → la gente que **te sigue**
- `following.html` → la gente que **vos seguís**

El resultado es una lista con los usuarios que **vos seguís, pero no te siguen de vuelta**.

---

## Requisitos
 
- Instalar la librería **BeautifulSoup4**

```bash
pip install beautifulsoup4
```
Si no te funciona pip, probá con:
```bash
python -m pip install beautifulsoup4
```
O
```bash
py -m pip install beautifulsoup4
```
## Instrucciones de uso

Descargá tu información desde Instagram:
Configuración → Centro de cuentas → Tu información y permisos → Descargar tu información

Elegí el formato HTML
Cuando te llegue el ZIP, abrilo y buscá dentro los archivos:

followers.html

following_1.html

Colocá esos archivos en la misma carpeta que el script no_me_siguen.py

Vas a ver en pantalla:
- Cuántos seguís
- Cuántos te siguen
- Y la lista de quienes vos seguís pero no te siguen
