import { detectarAlertaAmarilla } from "../modules/instructor/services/alertas";

const PushCheckIn = () => {
  const alertas = detectarAlertaAmarilla();

  const responder = (nombre, estado) => {
    const registro = {
      nombre,
      estado,
      fecha: new Date().toISOString(),
    };
    const prev = JSON.parse(localStorage.getItem('checkinPush')) || [];
    localStorage.setItem('checkinPush', JSON.stringify([...prev, registro]));
    alert(`Respuesta registrada para ${nombre}: ${estado}`);
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Notificaciones de Check-in</h2>
      {alertas.map((a, i) => (
        <div key={i} className="bg-yellow-100 p-4 rounded mb-3">
          <p>{a.mensaje}</p>
          <div className="flex gap-2 mt-2">
            <button className="btn bg-green-500 text-white" onClick={() => responder(a.aprendiz, 'Todo Bien')}>Todo Bien</button>
            <button className="btn bg-red-500 text-white" onClick={() => responder(a.aprendiz, 'Necesita Atención')}>Necesita Atención</button>
            <button className="btn bg-gray-400" onClick={() => responder(a.aprendiz, 'Recordar después')}>Recordar después</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default PushCheckIn;
