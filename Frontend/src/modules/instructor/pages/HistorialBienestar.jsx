import { useState, useEffect } from 'react';

const HistorialBienestar = () => {
  const [comunicaciones, setComunicaciones] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem('comunicacionesBienestar')) || [];
    setComunicaciones(data);
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Historial de Comunicaciones con Bienestar</h2>
      <ul className="space-y-4">
        {comunicaciones.map((c, i) => (
          <li key={i} className="bg-white p-4 shadow rounded">
            <p><strong>Aprendiz:</strong> {c.nombre}</p>
            <p><strong>Fecha:</strong> {c.fecha}</p>
            <p><strong>Motivo:</strong> {c.motivo}</p>
            <p><strong>Tipo:</strong> {c.tipo}</p>
            <p><strong>Mensaje:</strong> {c.mensaje}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HistorialBienestar;
