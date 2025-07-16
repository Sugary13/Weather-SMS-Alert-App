# ☔ Weather SMS Alert App

Este proyecto en Python consulta el pronóstico del clima usando la API de OpenWeatherMap y envía una alerta por SMS si se espera lluvia en las próximas horas utilizando el servicio de Twilio.

---

## 🚀 ¿Qué hace?

- Consume el pronóstico del clima a 12 horas (4 intervalos de 3h).
- Detecta condiciones de lluvia, nieve o tormenta (códigos de clima < 700).
- Envía un SMS automáticamente al usuario con un aviso para llevar paraguas ☔.

---

## 🛠 Tecnologías utilizadas

- Python 3
- [OpenWeatherMap API](https://openweathermap.org/forecast5)
- [Twilio API](https://www.twilio.com/)
- `requests` para consumir APIs REST
- `twilio` para enviar mensajes SMS

---

## 📦 Estructura del proyecto

.

├── main.py

├── README.md

└── requirements.txt

---

## 🔐 Configuración

1. Crea cuentas en:
   - [OpenWeatherMap](https://openweathermap.org/appid)
   - [Twilio](https://www.twilio.com/console)

2. Reemplaza tus credenciales en `main.py`:

```python
API_KEY = "TU_API_KEY_DE_OPENWEATHER"
LAT = TU_LATITUD
LON = TU_LONGITUD
account_sid = "TU_TWILIO_ACCOUNT_SID"
auth_token = "TU_AUTH_TOKEN"
```

3. Define tu número telefónico y el SID del servicio de mensajes de Twilio.

▶️ Cómo ejecutarlo

1. Instala dependencias:
```bash
   pip install requests twilio
```
2. Ejecuta el script:

```bash
python main.py
```

🧠 Explicación del código
- cnt=4 indica que se consultan 4 bloques de 3 horas (12 horas).

- weather['id'] < 700 identifica condiciones climáticas adversas (lluvia, tormenta, nieve).

- Si se cumplen, se crea y envía un SMS usando Twilio.

🌟 Posibles mejoras
- Agregar una interfaz de configuración con Tkinter

- Programar el script para que corra automáticamente cada mañana

- Enviar correo o notificación en vez de SMS

✍️ Autor
Carlos Esquerra Martínez
[Github](https://github.com/Sugary13)[LinkedIn](https://www.linkedin.com/in/carlos-esquerra-martinez-bba147269)

📜 Licencia
MIT © Carlos Esquerra Martínez

