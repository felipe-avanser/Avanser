import { useEffect, useState } from 'react';

const DashboardGeneral = () => {
  const [reportes, setReportes] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem('reportes')) || [];
    setReportes(data);
  }, []);

  const estudiantes = [...new Set(reportes.map(r => r.nombre))];
  const conReporte = [...new Set(reportes.filter(r => r.nivel || r.motivo).map(r => r.nombre))];
  const positivos = reportes.filter(r => r.nivel === 'Alto rendimiento');
  const alertas = reportes.filter(r => r.nivel === 'Problema actitudinal');

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Dashboard General</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-white p-4 shadow rounded">
          <p><strong>% con reportes este mes:</strong> {((conReporte.length / estudiantes.length) * 100).toFixed(1)}%</p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p><strong>% sin reportes:</strong> {(((estudiantes.length - conReporte.length) / estudiantes.length) * 100).toFixed(1)}%</p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p><strong>Balance:</strong> {positivos.length} positivos vs {alertas.length} alertas</p>
        </div>
      </div>

      <h3 className="text-lg font-semibold mt-6">Destacados del Mes</h3>
      <ul className="mt-2 space-y-2">
        {positivos.map((r, i) => (
          <li key={i} className="bg-green-100 p-2 rounded">{r.nombre}</li>
        ))}
      </ul>
    </div>
  );
};

export default DashboardGeneral;
