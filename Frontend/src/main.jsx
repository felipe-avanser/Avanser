/**
 * Archivo principal de arranque del frontend.
 *
 * Este archivo inicializa la aplicación React y la monta en el DOM.
 * 
 * Funciones principales:
 *  - Importa los módulos base de React (StrictMode, createRoot).
 *  - Importa los estilos globales de la aplicación.
 *  - Renderiza el componente raíz <App /> dentro del elemento HTML con id="root".
 *  - StrictMode ayuda a detectar prácticas no recomendadas durante el desarrollo.
 *
 * Proyecto: Avanser
 * Autor: [Tu nombre o equipo]
 * Fecha: [Fecha actual]
 */

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

// Crea el punto de montaje principal en el elemento con id="root"
// y renderiza el componente raíz <App /> dentro del modo estricto.
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
)
