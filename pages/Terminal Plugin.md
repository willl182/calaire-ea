## Logseq Terminal Plugin
	- ### ¿Qué es?
	  Plugin para Logseq que integra un emulador de terminal real dentro de la aplicación. Utiliza **xterm.js** para la emulación de terminal y **ttyd** como servidor WebSocket que conecta el navegador con un shell real (bash, zsh, fish).
- ### Características Principales
	- **Emulación de terminal completa**: Comportamiento nativo de terminal
	- **Soporte de teclado completo**: Flechas, backspace, historial de comandos, Ctrl+C, Ctrl+V
	- **Conexión WebSocket**: Se comunica con servidor ttyd en tiempo real
	- **Sincronización de tema**: Se adapta automáticamente al tema de Logseq (claro/oscuro)
	- **Dos modos de UI**:
		- Modal: Ventana emergente centrada
		- Panel: Panel lateral redimensionable
	- **Configuración personalizable**: Tamaño de fuente, servidor, puerto, etc.
	- **Conexión automática**: Se conecta al abrir el terminal
- ### Arquitectura
	- ```
	  ┌─────────────────────────────────────┐
	  │  Logseq Plugin (React + xterm.js) │
	  │  - Terminal UI                    │
	  │  - Theme sync                     │
	  │  - Settings                       │
	  └───────────────┬─────────────────┘
	                 │ WebSocket
	  ┌───────────────▼─────────────────┐
	  │  ttyd Server                     │
	  │  - WebSocket endpoint             │
	  │  - PTY management               │
	  └───────────────┬─────────────────┘
	                 │ PTY
	  ┌───────────────▼─────────────────┐
	  │  Shell (bash/zsh/fish)          │
	  │  - Command history               │
	  │  - Process execution            │
	  └─────────────────────────────────┘
	  ```
	- **Componentes**:
		- 1. **Logseq Plugin**: UI React + xterm.js para emulación de terminal
		  2. **ttyd**: Bridge WebSocket → PTY (pseudoterminal)
		  3. **Shell**: Procesa comandos como un terminal nativo
- ### Instalación
	- #### Paso 1: Instalar ttyd
		- ```bash
		  # macOS
		  brew install ttyd
		  
		  # Ubuntu/Debian
		  sudo apt install ttyd
		  
		  # Fedora
		  sudo dnf install ttyd
		  
		  # Arch Linux
		  sudo pacman -S ttyd
		  ```
	- #### Paso 2: Iniciar servidor ttyd
		- ```bash
		  # Básico con bash
		  ttyd -p 7681 bash
		  
		  # Con zsh
		  ttyd -p 7681 zsh
		  
		  # En background
		  ttyd -p 7681 bash &
		  ```
		  
		  **Nota**: ttyd debe estar corriendo antes de usar el plugin.
	- #### Paso 3: Instalar el plugin
		- 1. Descargar la última versión del plugin
		  2. En Logseq: **Settings** → **Plugins** → **Load unpacked plugin**
		  3. Seleccionar la carpeta del plugin
- ### Uso
	- #### Abrir el terminal
	- **Toolbar**: Click en icono de terminal (modal) o icono de sidebar (panel)
	- **Teclado**: `Ctrl+Shift+T` para modal o `Ctrl+`` para panel
	- **Slash command**: Escribir `/Terminal` en cualquier bloque
	- **Command Palette**: Escribir "Terminal" y seleccionar modo preferido
	- #### Características del terminal
	  Una vez abierto, se comporta como un terminal nativo:
		- **Historial de comandos**: `↑`/`↓` para navegar comandos anteriores
		- **Editar comandos**: `←`/`→` y `Backspace`/`Delete`
		- **Copiar/Pegar**: `Ctrl+C`/`Ctrl+V` (portapapeles nativo)
		- **Autocompletar**: `Tab` para autocompletar
		- **Interrumpir procesos**: `Ctrl+C`
	- Todos los atajos de teclado funcionan como se espera en un terminal estándar.
	- #### Modos de UI
		- **Modal**: Ventana emergente centrada (cerrar con botón ✕)
		- **Panel**: Panel lateral redimensionable (arrastrar el borde)
- ### Configuración
	- Navegar a **Settings** → **Plugins** → **Terminal**:
		- | Configuración | Default | Descripción |
		  |---------------|---------|-------------|
		  | Server Host | localhost | Host del servidor ttyd |
		  | Server Port | 7681 | Puerto del servidor ttyd |
		  | Protocol | ws | Protocolo WebSocket (ws/wss) |
		  | Font Size | 14 | Tamaño de fuente del terminal |
		  | Font Family | Menlo, Monaco... | Familia de fuente |
		  | Scrollback | 1000 | Líneas en el buffer |
		  | Auto Connect | true | Conectar automáticamente al abrir |
- ### Troubleshooting
	- #### "Failed to connect to ttyd server"
		- 1. **Verificar si ttyd está corriendo**:
			- ```bash
			   ps aux | grep ttyd
			   ```
		- 2. **Verificar que el puerto está escuchando**:
			- ```bash
			   lsof -i :7681
			   # o
			   netstat -an | grep 7681
			   ```
		- 3. **Asegurar que las configuraciones coinciden**:
			- Host: Debe coincidir con donde está ttyd (localhost si es misma máquina)
			- Port: Debe coincidir con el puerto usado al iniciar ttyd
	- #### Atajos de teclado no funcionan
		- Asegurar que el terminal tiene foco (click dentro de la ventana del terminal). xterm.js maneja todos los eventos de teclado nativamente.
	- #### Terminal aparece congelado
		- 1. Verificar consola del navegador para errores (F12)
		  2. Verificar que ttyd sigue corriendo
		  3. Intentar desconectar y reconectar
- ### Estructura del Proyecto
	- ```
	  terminal_plugin/
	  ├── src/
	  │   ├── components/
	  │   │   ├── ConnectionStatus.tsx
	  │   │   ├── Terminal.tsx
	  │   │   ├── TerminalHeader.tsx
	  │   │   ├── TerminalModal.tsx
	  │   │   └── TerminalPanel.tsx
	  │   ├── lib/
	  │   │   ├── graphPath.ts
	  │   │   ├── settings.ts
	  │   │   ├── theme.ts
	  │   │   └── ttydClient.ts
	  │   ├── styles/
	  │   │   ├── index.ts
	  │   │   └── terminal.css
	  │   ├── types/
	  │   │   └── global.d.ts
	  │   ├── App.tsx
	  │   └── main.tsx
	  ├── README.md
	  ├── package.json
	  ├── tsconfig.json
	  └── vite.config.ts
	  ```
- ### Tecnologías Utilizadas
	- **React**: Framework UI para el plugin
	- **xterm.js**: Emulador de terminal en JavaScript
	- **ttyd**: Bridge WebSocket a PTY
	- **TypeScript**: Tipado estático
	- **Vite**: Build tool
- ### Conclusión
	- Plugin muy útil que permite ejecutar comandos de terminal directamente desde Logseq sin cambiar de aplicación. La arquitectura usando ttyd como puente WebSocket es elegante y permite una experiencia de terminal completa.