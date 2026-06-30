import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import React from 'react';
import Header from './components/Header';
import Nav from './components/Nav';
import Footer from './components/Footer';

import inicio from './pages/inicio';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Nav />
      <Footer />
    </BrowserRouter>
  );
}

export default App;