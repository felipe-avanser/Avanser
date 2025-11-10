import { useState } from 'react';
import Navbar from '../../../components/Navbar';

const BienestarComunicacion = () => {
  const [form, setForm] = useState({
    nombre: '',
    fecha: '',
    motivo: '',
    tipo: '',
    mensaje: '',
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const enviar = () => {
    if (!form.nombre || !form.fecha || !form.motivo || !form.tipo || !form.mensaje) {
      alert('Completa todos los campos');
      return;
    }
    const prev = JSON.parse(localStorage.getItem('comunicacionesBienestar')) || [];
    localStorage.setItem('comunicacionesBienestar', JSON.stringify([...prev, form]));
    alert('Comunicación enviada a Bienestar');
  };

  return (
    <div className="p-6 max-w-xl mx-auto bg-white shadow rounded">
         <Navbar />
      <h2 className="text-xl font-bold mb-4">Comunicación a Bienestar</h2>
      <input name="nombre" placeholder="Nombre del aprendiz" onChange={handleChange} className="input" />
      <input name="fecha" type="date" onChange={handleChange} className="input" />
      <input name="motivo" placeholder="Motivo" onChange={handleChange} className="input" />
      <select name="tipo" onChange={handleChange} className="input">
        <option value="">Tipo de comunicación</option>
        <option value="Académico">Académico</option>
        <option value="Convivencial">Convivencial</option>
        <option value="Psicosocial">Psicosocial</option>
      </select>
      <textarea name="mensaje" placeholder="Mensaje" onChange={handleChange} className="input" />
      <button className="btn bg-purple-600 text-white mt-2" onClick={enviar}>Enviar a Bienestar</button>
    </div>
  );
};

export default BienestarComunicacion;
