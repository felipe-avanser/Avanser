import { useEffect, useState } from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";
import { detectarAlertaRoja, detectarAlertaAmarilla } from "../services/alertas";

ChartJS.register(ArcElement, Tooltip, Legend);

const DashboardFinal = () => {
  const [reportes, setReportes] = useState([]);
  const [alertasRoja, setAlertasRoja] = useState([]);
  const [alertasAmarilla, setAlertasAmarilla] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("reportes")) || [];
    setReportes(data);

    // Detectar alertas
    setAlertasRoja(detectarAlertaRoja());
    setAlertasAmarilla(detectarAlertaAmarilla());
  }, []);

  // Calcular estadísticas
  const estudiantes = [...new Set(reportes.map((r) => r.nombre))];
  const conReporte = [...new Set(reportes.map((r) => r.nombre))];
  const positivos = reportes.filter((r) => r.nivel === "Alto rendimiento");
  const alertas = reportes.filter((r) => r.nivel === "Problema actitudinal");

  // Datos para gráfica
  const tipoCounts = reportes.reduce((acc, r) => {
    const tipo = r.nivel || r.motivo || "Otro";
    acc[tipo] = (acc[tipo] || 0) + 1;
    return acc;
  }, {});

  const pieData = {
    labels: Object.keys(tipoCounts),
    datasets: [
      {
        data: Object.values(tipoCounts),
        backgroundColor: ["#4ade80", "#60a5fa", "#f87171", "#fbbf24"],
      },
    ],
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Dashboard General</h2>

      {/* Estadísticas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="bg-white p-4 shadow rounded">
          <p>
            <strong>% con reportes este mes:</strong>{" "}
            {((conReporte.length / estudiantes.length) * 100 || 0).toFixed(1)}%
          </p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p>
            <strong>% sin reportes:</strong>{" "}
            {(((estudiantes.length - conReporte.length) / estudiantes.length) *
              100 || 0).toFixed(1)}
            %
          </p>
        </div>
        <div className="bg-white p-4 shadow rounded">
          <p>
            <strong>Balance:</strong> {positivos.length} positivos vs{" "}
            {alertas.length} alertas
          </p>
        </div>
      </div>

      {/* Alertas */}
      <h3 className="text-lg font-semibold mb-2">Alertas Automáticas</h3>
      <div className="space-y-2 mb-6">
        {alertasRoja.map((a, i) => (
          <div key={i} className="bg-red-100 p-3 rounded">
            🔴 {a.mensaje}
          </div>
        ))}
        {alertasAmarilla.map((a, i) => (
          <div key={i} className="bg-yellow-100 p-3 rounded">
            🟡 {a.mensaje}
          </div>
        ))}
        {alertasRoja.length === 0 && alertasAmarilla.length === 0 && (
          <p className="text-gray-500">No hay alertas activas</p>
        )}
      </div>

      {/* Gráfica */}
      <h3 className="text-lg font-semibold mb-2">Distribución de Reportes</h3>
      <div className="max-w-md mx-auto mb-6">
        <Pie data={pieData} />
      </div>

      {/* Reconocimiento */}
      <h3 className="text-lg font-semibold mb-2">🌟 Destacados del Mes</h3>
      <ul className="space-y-2">
        {positivos.map((r, i) => (
          <li key={i} className="bg-green-100 p-2 rounded">
            {r.nombre}
          </li>
        ))}
        {positivos.length === 0 && (
          <p className="text-gray-500">No hay estudiantes destacados aún</p>
        )}
      </ul>
    </div>
  );
};

export default DashboardFinal;
