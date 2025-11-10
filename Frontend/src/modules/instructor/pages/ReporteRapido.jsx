import { useState } from 'react';

const niveles = ['Alto rendimiento', 'Medio rendimiento', 'Bajo rendimiento', 'Problema actitudinal'];

const ReporteRapido = () => {
  const [nombre, setNombre] = useState('');
  const [nivel, setNivel] = useState('');

  const guardar = () => {
    if (!nombre || !nivel) return alert('Completa los campos');
    const nuevo = { nombre, nivel, fecha: new Date().toISOString() };
    const prev = JSON.parse(localStorage.getItem('reportes')) || [];
    localStorage.setItem('reportes', JSON.stringify([...prev, nuevo]));
    alert('Reporte guardado');
  };

  return (
    <div className="p-6 max-w-md mx-auto bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4">Reporte Rápido</h2>
      <input placeholder="Nombre del aprendiz" value={nombre} onChange={e => setNombre(e.target.value)} className="input" />
      <select value={nivel} onChange={e => setNivel(e.target.value)} className="input">
        <option value="">Selecciona nivel</option>
        {niveles.map((n, i) => <option key={i} value={n}>{n}</option>)}
      </select>
      <button className="btn bg-blue-600 text-white mt-2" onClick={guardar}>Guardar</button>
    </div>
  );
};

export default ReporteRapido;
