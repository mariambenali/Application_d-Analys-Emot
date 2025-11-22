import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {BrowserRouter,Routes, Route} from "react-router-dom"
import { useNavigate } from 'react-router-dom'

import './login_page/login.css'
import Login from "./login_page/login.jsx"
import './dash_page/dashboard.css'
import Dashboard from "./dash_page/dashboard.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/predict" element={<Dashboard/>} />

        <Route path="/" element={<Login/>} />

      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
