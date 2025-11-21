import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './login_page/login.css'
import App from './App.jsx'
import Login from "./login_page/login.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    
    <Login/>
  </StrictMode>,
)
