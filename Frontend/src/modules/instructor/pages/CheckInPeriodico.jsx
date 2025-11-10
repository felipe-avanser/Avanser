import { useState } from 'react';
import Navbar from '../../../components/Navbar';
const estudiantesDemo = Array.from({ length: 20 }, (_, i) => ({
  id: i + 1,
  nombre: `Aprendiz ${i + 1}`,
}));

const CheckInPeriodico = () => {
  const [estado, setEstado] = useState({});

  const marcarEstado = (id, tipo, valor) => {
    setEstado(prev => ({
      ...prev,
      [id]: { ...prev[id], [tipo]: valor },
    }));
  };

  const guardar = () => {
    const prev = JSON.parse(localStorage.getItem('checkin')) || [];
    const nuevo = estudiantesDemo.map(e => ({
      nombre: e.nombre,
      estado: estado[e.id] || {},
      fecha: new Date().toISOString(),
    }));
    localStorage.setItem('checkin', JSON.stringify([...prev, ...nuevo]));
    alert('Check-in guardado');
  };

  return (
    <div className="p-6">
         <Navbar />
      <h2 className="text-xl font-bold mb-4">Check-in Quincenal</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {estudiantesDemo.map(e => (
          <div key={e.id} className="bg-white p-4 shadow rounded">
            <p className="font-semibold">{e.nombre}</p>
            <select onChange={e => marcarEstado(e.id, 'academico', e.target.value)} className="input">
              <option value="">Académico</option>
              <option value="Bien">Bien</option>
              <option value="Regular">Regular</option>
              <option value="Mal">Mal</option>
            </select>
            <select onChange={e => marcarEstado(e.id, 'social', e.target.value)} className="input">
              <option value="">Social</option>
              <option value="Bien">Bien</option>
              <option value="Regular">Regular</option>
              <option value="Mal">Mal</option>
            </select>
          </div>
        ))}
      </div>
      <button className="btn bg-green-600 text-white mt-4" onClick={guardar}>Guardar Check-in</button>
    </div>
  );
};

export default CheckInPeriodico;
