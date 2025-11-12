import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

const VistaAprendizConvocatorias = () => {
  const [convocatorias, setConvocatorias] = useState([]);

  useEffect(() => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    // Filtrar solo las activas y con cupos disponibles
    const disponibles = todas.filter((c) => {
      const inscritos = c.inscripciones ? c.inscripciones.length : 0;
      const cuposLlenos = inscritos >= Number(c.cupos);
      return c.estado === "Activa" && !cuposLlenos;
    });
    setConvocatorias(disponibles);
  }, []);

  if (convocatorias.length === 0) {
    return (
      <div className="p-6 text-center">
        No hay convocatorias disponibles para inscripción en este momento.
      </div>
    );
  }

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Convocatorias disponibles</h2>
      <table className="w-full border-collapse border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">Título</th>
            <th className="border p-2">Tipo</th>
            <th className="border p-2">Inicio</th>
            <th className="border p-2">Cierre</th>
            <th className="border p-2">Cupos</th>
            <th className="border p-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {convocatorias.map((c) => {
            const inscritos = c.inscripciones ? c.inscripciones.length : 0;
            return (
              <tr key={c.id}>
                <td className="border p-2">{c.titulo}</td>
                <td className="border p-2">{c.tipo}</td>
                <td className="border p-2">{c.inicio}</td>
                <td className="border p-2">{c.cierre}</td>
                <td className="border p-2 text-center">
                  {inscritos} / {c.cupos}
                </td>
                <td className="border p-2 text-center">
                  <Link
                    to={`/inscripcion-convocatoria/${c.id}`}
                    className="bg-purple-500 text-white px-2 py-1 rounded hover:bg-purple-600"
                  >
                    Inscribirme
                  </Link>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default VistaAprendizConvocatorias;
