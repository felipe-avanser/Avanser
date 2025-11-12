import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const DetalleConvocatoria = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [convocatoria, setConvocatoria] = useState(null);

  useEffect(() => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const encontrada = todas.find((c) => c.id === Number(id));
    setConvocatoria(encontrada);
  }, [id]);

  const actualizarEstado = (nuevoEstado, mensaje) => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const actualizadas = todas.map((c) =>
      c.id === Number(id)
        ? {
            ...c,
            estado: nuevoEstado,
            historial: [
              ...(c.historial || []),
              { estado: nuevoEstado, fecha: new Date().toLocaleString() },
            ],
          }
        : c
    );
    localStorage.setItem("convocatorias", JSON.stringify(actualizadas));
    alert(mensaje);
    navigate(`/detalle-convocatoria/${id}`);
  };

  if (!convocatoria) {
    return <div className="p-6 text-center">Convocatoria no encontrada.</div>;
  }

  const inscritos = convocatoria.inscripciones ? convocatoria.inscripciones.length : 0;
  const cuposLlenos = inscritos >= Number(convocatoria.cupos);

  return (
    <div className="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
      <h2 className="text-2xl font-bold mb-4">{convocatoria.titulo}</h2>

      <p className="mb-2">
        <strong>Tipo:</strong> {convocatoria.tipo}
      </p>
      <p className="mb-2">
        <strong>Estado:</strong> {convocatoria.estado}
        {cuposLlenos && (
          <span className="ml-2 inline-block bg-orange-500 text-white text-xs px-2 py-1 rounded">
            Cupos llenos
          </span>
        )}
      </p>
      <p className="mb-2"><strong>Inicio:</strong> {convocatoria.inicio}</p>
      <p className="mb-2"><strong>Cierre:</strong> {convocatoria.cierre}</p>
      <p className="mb-2"><strong>Cupos disponibles:</strong> {convocatoria.cupos}</p>
      <p className="mb-2">
        <strong>Inscritos:</strong> {inscritos} / {convocatoria.cupos}
      </p>

      <div className="mt-4">
        <strong>Descripción:</strong>
        <div
          className="mt-2 p-4 bg-gray-100 rounded"
          dangerouslySetInnerHTML={{ __html: convocatoria.descripcion }}
        />
      </div>

      {convocatoria.estado === "Borrador" && (
        <button
          onClick={() => actualizarEstado("Activa", "✅ Convocatoria publicada exitosamente")}
          className="mt-6 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-all"
        >
          Publicar convocatoria
        </button>
      )}

      {convocatoria.estado === "Activa" && (
        <div className="mt-6 flex gap-3">
          <button
            onClick={() => actualizarEstado("Cerrada", "🚫 Convocatoria cerrada, ya no se aceptan inscripciones")}
            className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition-all"
          >
            Cerrar convocatoria
          </button>
          {cuposLlenos && (
            <span className="inline-block bg-gray-500 text-white px-3 py-2 rounded">
              Inscripciones no disponibles (cupos llenos)
            </span>
          )}
        </div>
      )}

      {convocatoria.estado === "Cerrada" && (
        <button
          onClick={() => actualizarEstado("Activa", "🔄 Convocatoria reabierta, inscripciones habilitadas nuevamente")}
          className="mt-6 bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700 transition-all"
        >
          Reabrir convocatoria
        </button>
      )}

      {convocatoria.inscripciones && convocatoria.inscripciones.length > 0 && (
        <div className="mt-8">
          <h3 className="text-xl font-semibold mb-4">Lista de inscritos</h3>
          <table className="w-full border-collapse border border-gray-300">
            <thead>
              <tr className="bg-gray-100">
                <th className="border p-2">Nombre</th>
                <th className="border p-2">Documento</th>
                <th className="border p-2">Fecha de inscripción</th>
              </tr>
            </thead>
            <tbody>
              {convocatoria.inscripciones.map((i, index) => (
                <tr key={index}>
                  <td className="border p-2">{i.nombre}</td>
                  <td className="border p-2">{i.documento}</td>
                  <td className="border p-2">{i.fecha}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {convocatoria.historial && convocatoria.historial.length > 0 && (
        <div className="mt-8">
          <h3 className="text-xl font-semibold mb-4">Historial de cambios de estado</h3>
          <ul className="list-disc pl-6">
            {convocatoria.historial.map((h, index) => (
              <li key={index}>
                {h.estado} — {h.fecha}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default DetalleConvocatoria;
