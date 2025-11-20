# 🚀 NEXTIA TOKEN PRESALE - SETUP COMPLETO

**Fecha:** 19 de Noviembre 2025  
**Status:** ✅ Listo para deployar  
**Objetivo:** Captar inversores para presale (Meta: $40K+)

---

## 📂 ARCHIVOS QUE YA TIENES

```
/proyectos/nextia/marketing/
│
├── landing_presale_moderna.html       ← LANDING PAGE (principal)
├── whitelist_form_moderno.html        ← FORMULARIO DE REGISTRO
├── thank_you_moderno.html             ← PÁGINA DE GRACIAS
│
├── twitter_automation.py              ← SCRIPT PARA AUTOMATIZAR TWITTER
├── env_example.txt                    ← PLANTILLA DE CONFIGURACIÓN
│
└── README.md                          ← ESTE ARCHIVO
```

---

## 🎯 ¿QUÉ HACE CADA ARCHIVO?

### 1. **landing_presale_moderna.html**
**Qué es:** Tu página principal bonita  
**Dónde la ven:** https://nextia-presale.vercel.app  
**Qué tiene:**
- Hero section con info del proyecto
- Características (6 cards)
- Tokenomics en detalle
- Roadmap visual
- Stats en vivo
- CTA (llamado a acción) para registrarse
- Footer con links

**Cómo se ve:** Moderna, oscura, colores degradados (azul-púrpura), responsiva

---

### 2. **whitelist_form_moderno.html**
**Qué es:** Formulario para captar emails  
**Dónde va:** Link en landing page  
**Qué captura:**
- Email (requerido)
- Nombre
- Usuario Telegram
- Wallet address
- Comentarios

**A dónde van los datos:** A Formspree → a tu email (nextiacorp33@gmail.com)

---

### 3. **thank_you_moderno.html**
**Qué es:** Página de confirmación  
**Cuándo aparece:** Después de completar el formulario  
**Qué muestra:**
- ✅ Mensaje de éxito
- Checklist de beneficios
- Links a Telegram/Discord
- Cronómetro del presale

---

### 4. **twitter_automation.py**
**Qué es:** Script para publicar tweets automáticamente  
**Requiere:** Credenciales de Twitter API  
**Funciones:**
- Publicar tweets individuales
- Publicar threads (múltiples tweets)
- Agendar tweets para horarios específicos
- Tweets pre-escritos sobre presale, staking, comunidad

---

## 📋 PASO A PASO - SETUP FINAL

### PASO 1: Descargar los archivos HTML

Estos 3 archivos ya los tienes. Cópialos a tu carpeta:

```bash
# En terminal
cd /proyectos/nextia/marketing/landing-presale

# Verifica que esté el HTML
ls -la
# Deberías ver: landing_presale_moderna.html
```

Si no lo ves, copia el contenido manualmente en un archivo nuevo.

---

### PASO 2: Configurar Formspree

**Paso 2A: Ir a Formspree**
1. Ve a https://formspree.io
2. Sign Up con tu email (nextiacorp33@gmail.com)
3. Verifica tu email

**Paso 2B: Crear un formulario**
1. En dashboard → "Create Form"
2. Nombre: `NextiaWhitelist`
3. Email destino: `nextiacorp33@gmail.com`
4. Clic en "Create"

**Paso 2C: Copiar el código**
Formspree te muestra algo como:
```
Form ID: f/xxxxxxxx
```
Ejemplo: `f/m1a2b3c4d5e6f7g8`

**Paso 2D: Actualizar los HTML**

En los archivos HTML (`landing_presale_moderna.html` y `whitelist_form_moderno.html`), busca:

```html
action="https://formspree.io/f/REEMPLAZA_AQUI"
```

Y reemplaza `REEMPLAZA_AQUI` con tu código de Formspree.

Ejemplo:
```html
action="https://formspree.io/f/m1a2b3c4d5e6f7g8"
```

---

### PASO 3: Publicar en Vercel

**Paso 3A: Deploy**

```bash
cd /proyectos/nextia/marketing/landing-presale
vercel --prod
```

Responde las preguntas:
```
? Set up and deploy? [Y/n]: Y
? Project name: nextia-presale
? Directory: [.]:  (presiona Enter)
```

**Paso 3B: Guardar la URL**
Vercel te da:
```
✅ Production: https://nextia-presale.vercel.app
```

Guarda esa URL. La necesitarás para social media.

---

### PASO 4: Obtener credenciales de Twitter API

**Paso 4A: Developer Portal**
1. Ve a https://developer.twitter.com/en/portal/dashboard
2. Crea una app (si no tienes)
3. En "Keys and tokens" obtén:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret

**Paso 4B: Crear archivo .env**

En `/proyectos/nextia/marketing/`:

```bash
nano .env
```

Pega esto (reemplazando con tus credenciales reales):

```env
TWITTER_API_KEY=abc123xyz...
TWITTER_API_SECRET=def456...
TWITTER_ACCESS_TOKEN=ghi789...
TWITTER_ACCESS_SECRET=jkl012...
```

Guarda con: `Ctrl + X`, `Y`, `Enter`

---

### PASO 5: Instalar dependencias Python

```bash
cd /proyectos/nextia/marketing
pip install tweepy python-dotenv schedule
```

---

### PASO 6: Probar publicar un tweet

```bash
python twitter_automation.py --presale
```

Esto publica 3 tweets de presale automáticamente. Si ves 3 ✅ verdes, ¡funciona!

---

## 🎨 PERSONALIZACIONES IMPORTANTES

### 1. Cambiar links de redes sociales

En los archivos HTML, busca y actualiza:

```html
<!-- Telegram -->
href="https://t.me/nextiatokenoficial"

<!-- Discord -->
href="https://discord.gg/nextia"

<!-- Twitter -->
href="https://twitter.com/nextia33"

<!-- GitHub -->
href="https://github.com/NextiaLabs"
```

Reemplaza con TUS canales/links.

### 2. Cambiar información del token

En landing page, actualiza:
- Nombres (Nextia Token → tu nombre)
- APY (20% → tu porcentaje)
- Precios de presale
- Fechas del roadmap
- Links a tus repos

### 3. Cambiar colores

En los CSS, busca `:root` y modifica:

```css
:root {
    --primary: #667eea;        ← Color principal
    --primary-dark: #764ba2;   ← Color oscuro
    --accent: #ff006e;         ← Color de acento
}
```

---

## 📊 ESTRUCTURA FINAL

Tu setup completo:

```
LANDING PAGE
    ↓
    (Navegador abierto)
    ↓
    USUARIO VE INFORMACIÓN DEL TOKEN
    ↓
    HACE CLIC EN "UNIRSE"
    ↓
    VA AL FORMULARIO
    ↓
    INGRESA EMAIL + DATOS
    ↓
    FORMSPREE RECIBE EL EMAIL
    ↓
    TÚ RECIBIS NOTIFICACIÓN EN nextiacorp33@gmail.com
    ↓
    USUARIO VE PÁGINA DE GRACIAS
    ↓
    USUARIO SE UNE A TELEGRAM (link en página)
```

---

## 🚀 PRÓXIMO PASO (Mañana)

1. Verifica que el formulario funciona
2. Publica 3 tweets con twitter_automation.py
3. Comparte landing page en redes sociales
4. Revisa que chegaron emails a nextiacorp33@gmail.com

---

## ❌ SI ALGO FALLA

**Formulario no envía:**
- Verifica que reemplazaste REEMPLAZA_AQUI con el código de Formspree
- Comprueba que el archivo está en UTF-8

**Vercel dice error:**
- Ejecuta: `npm install -g vercel`
- Intenta deploy nuevamente

**Twitter no publica:**
- Verifica que .env tiene credenciales CORRECTAS
- Comprueba que tienes acceso a Twitter API
- Intenta con: `python twitter_automation.py --tweet "Hola mundo"`

---

## 📞 RESUMEN RÁPIDO

| Tarea | Archivo | Status |
|-------|---------|--------|
| Landing page moderna | landing_presale_moderna.html | ✅ |
| Formulario whitelist | whitelist_form_moderno.html | ✅ |
| Página de gracias | thank_you_moderno.html | ✅ |
| Automatización Twitter | twitter_automation.py | ✅ |
| Configuración | .env | ⏳ Pendiente |
| Deployment Vercel | vercel --prod | ⏳ Pendiente |

---

## 🎯 METAS PARA ESTA SEMANA

- ✅ Setup completo (HOY)
- ✅ Primeros 50 emails registrados (Día 2-3)
- ✅ 500+ seguidores en redes (Día 4-5)
- ✅ $10K+ en presale (Fin de semana)

---

**¿Listo bro? Empecemos a captar inversores. 🚀**