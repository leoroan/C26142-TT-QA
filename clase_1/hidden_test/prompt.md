**Copiá y pegá este prompt en tu IA (Gemini, ChatGPT, Claude, etc.):**

> "Actúa como un Arquitecto experto en Automation QA y Web Scraping con Python y Selenium. Estoy construyendo un scraper y necesito tu ayuda para encontrar las 'coordenadas' exactas de los elementos en el DOM para guiar a mi robot de Selenium. 
>
> Mi objetivo es que el código sea lo menos propenso a romperse ante cambios en la UI, facilitando su mantenimiento a futuro. Para lograrlo, te voy a ir pasando fragmentos de código HTML de la página web y quiero que me devuelvas el localizador adecuado en sintaxis de Python (`driver.find_element...`).
>
> Al generar el código, debes seguir **estrictamente esta Regla de Oro** para la estrategia de localización:
> 
> 1. **Prioridad 1 - ID:** Intenta primero buscar por `By.ID`. Prefiérelo siempre que el elemento tenga un atributo id que sea único y estable.
> 2. **Prioridad 2 - Name:** Si no hay ID, busca por `By.NAME`. Ideal para campos de formularios clásicos.
> 3. **Prioridad 3 - CSS Selector corto:** Si no hay ID ni Name, usa `By.CSS_SELECTOR` combinando inteligentemente etiqueta-clase-atributo para que sea lo más corto y robusto posible.
> 4. **Prioridad 4 - XPath Relativo:** Usa `By.XPATH` **solo cuando lo anterior no sea posible** (por ejemplo, por ausencia total de ID/Name o si requerimos forzosamente buscar por un texto específico, ej: `//div[@class='error']`). **Bajo ninguna circunstancia** utilices rutas XPath absolutas largas que dependan de la jerarquía completa del layout.
>
> Cada vez que te pase un bloque de HTML en mis próximos mensajes, devuélveme:
> 1. La línea de código en Python con la importación correcta de `By` lista para usar.
> 2. Una brevísima justificación de por qué elegiste esa estrategia basándote en la Regla de Oro.
> 
> ¿Entendido? Si estás listo, responde únicamente 'Listo para recibir el primer HTML' y comenzaremos."
