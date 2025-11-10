import { useState, useEffect } from 'react';

const ReportesPage = () => {
  const [reportes, setReportes] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem('reportes')) || [];
    setReportes(data);
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Listado de Reportes</h2>
      <ul className="space-y-4">
        {reportes.map((r, i) => (
          <li key={i} className="bg-white shadow p-4 rounded">
            <p><strong>Aprendiz:</strong> {r.nombre}</p>
            <p><strong>Motivo:</strong> {r.motivo}</p>
            <button
              className="mt-2 bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
              onClick={() => alert(`Citando a comité a ${r.nombre}`)}
            >
              Citar a Comité
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReportesPage;
