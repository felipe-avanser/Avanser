import { useEffect, useState } from 'react';
import { Bar, Pie } from 'react-chartjs-2';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(BarElement, CategoryScale, LinearScale, ArcElement, Tooltip, Legend);

const DashboardCharts = () => {
  const [reportes, setReportes] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem('reportes')) || [];
    setReportes(data);
  }, []);

  const tipoCounts = reportes.reduce((acc, r) => {
    const tipo = r.nivel || r.motivo || 'Otro';
    acc[tipo] = (acc[tipo] || 0) + 1;
    return acc;
  }, {});

  const pieData = {
    labels: Object.keys(tipoCounts),
    datasets: [
      {
        data: Object.values(tipoCounts),
        backgroundColor: ['#4ade80', '#60a5fa', '#f87171', '#fbbf24'],
      },
    ],
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Gráficas de Reportes</h2>
      <div className="max-w-md mx-auto">
        <Pie data={pieData} />
      </div>
    </div>
  );
};

export default DashboardCharts;
