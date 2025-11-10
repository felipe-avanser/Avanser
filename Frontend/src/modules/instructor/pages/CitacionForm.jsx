import { useState } from 'react';

const CitacionForm = () => {
  const [form, setForm] = useState({
    nombre: '',
    fecha: '',
    hora: '',
    motivo: '',
    actores: '',
    nota: '',
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const guardarCitacion = () => {
    if (!form.nombre || !form.fecha || !form.hora || !form.motivo) {
      alert('Por favor completa los campos obligatorios');
      return;
    }
    const prev = JSON.parse(localStorage.getItem('citaciones')) || [];
    localStorage.setItem('citaciones', JSON.stringify([...prev, form]));
    alert('Citación creada');
  };

  return (
    <div className="p-6 max-w-xl mx-auto bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4">Crear Citación</h2>
      <input name="nombre" placeholder="Nombre del aprendiz" onChange={handleChange} className="input" />
      <input name="fecha" type="date" onChange={handleChange} className="input" />
      <input name="hora" type="time" onChange={handleChange} className="input" />
      <input name="motivo" placeholder="Motivo" onChange={handleChange} className="input" />
      <input name="actores" placeholder="Actores involucrados" onChange={handleChange} className="input" />
      <textarea name="nota" placeholder="Nota breve (140+ caracteres)" onChange={handleChange} className="input" />
      <div className="flex gap-2 mt-4">
        <button className="btn bg-gray-300">Eliminar</button>
        <button className="btn bg-yellow-400">Guardar Borrador</button>
        <button className="btn bg-green-600 text-white" onClick={guardarCitacion}>Crear Citación</button>
      </div>
    </div>
  );
};

export default CitacionForm;
