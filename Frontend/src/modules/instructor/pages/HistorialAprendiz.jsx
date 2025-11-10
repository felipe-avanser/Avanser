import { useState, useEffect } from 'react';

const HistorialAprendiz = () => {
  const [nombre, setNombre] = useState('');
  const [historial, setHistorial] = useState([]);

  const buscarHistorial = () => {
    const reportes = JSON.parse(localStorage.getItem('reportes')) || [];
    const filtrados = reportes.filter(r => r.nombre.toLowerCase() === nombre.toLowerCase());
    setHistorial(filtrados);
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Historial de Reportes</h2>
      <input
        type="text"
        placeholder="Nombre del aprendiz"
        value={nombre}
        onChange={e => setNombre(e.target.value)}
        className="input"
      />
      <button className="btn bg-blue-600 text-white mt-2" onClick={buscarHistorial}>Buscar</button>

      <ul className="mt-4 space-y-3">
        {historial.map((r, i) => (
          <li key={i} className="bg-white p-4 shadow rounded">
            <p><strong>Fecha:</strong> {new Date(r.fecha).toLocaleDateString()}</p>
            <p><strong>Motivo:</strong> {r.motivo || r.nivel}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HistorialAprendiz;
