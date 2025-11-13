import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

const ListadoConvocatorias = () => {
  const [convocatorias, setConvocatorias] = useState([]);
  const [filtro, setFiltro] = useState("Todas");

  useEffect(() => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    setConvocatorias(todas);
  }, []);

  const filtradas =
    filtro === "Todas"
      ? convocatorias
      : convocatorias.filter((c) => c.estado === filtro);

  if (convocatorias.length === 0) {
    return <div className="p-6 text-center">No hay convocatorias registradas.</div>;
  }

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Listado de Convocatorias</h2>

      {/* Filtros */}
      <div className="mb-4 flex gap-2">
        {["Todas", "Borrador", "Activa", "Cerrada"].map((estado) => (
          <button
            key={estado}
            onClick={() => setFiltro(estado)}
            className={`px-3 py-1 rounded ${
              filtro === estado
                ? "bg-blue-600 text-white"
                : "bg-gray-200 hover:bg-gray-300"
            }`}
          >
            {estado}
          </button>
        ))}
      </div>

      <table className="w-full border-collapse border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">Título</th>
            <th className="border p-2">Tipo</th>
            <th className="border p-2">Estado</th>
            <th className="border p-2">Inscritos</th>
            <th className="border p-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {filtradas.map((c) => {
            const inscritos = c.inscripciones ? c.inscripciones.length : 0;
            const cuposLlenos = inscritos >= Number(c.cupos);

            return (
              <tr key={c.id}>
                <td className="border p-2">{c.titulo}</td>
                <td className="border p-2">{c.tipo}</td>
                <td className="border p-2">
                  {c.estado}
                  {cuposLlenos && (
                    <span className="ml-2 inline-block bg-orange-500 text-white text-xs px-2 py-1 rounded">
                      Cupos llenos
                    </span>
                  )}
                </td>
                <td className="border p-2 text-center">
                  {inscritos} / {c.cupos}
                </td>
                <td className="border p-2 text-center">
                  <Link
                    to={`/detalle-convocatoria/${c.id}`}
                    className="bg-blue-500 text-white px-2 py-1 rounded mr-2 hover:bg-blue-600"
                  >
                    Ver
                  </Link>
                  <Link
                    to={`/editar-convocatoria/${c.id}`}
                    className="bg-green-500 text-white px-2 py-1 rounded mr-2 hover:bg-green-600"
                  >
                    Editar
                  </Link>

                  {c.estado === "Activa" && !cuposLlenos && (
                    <Link
                      to={`/inscripcion-convocatoria/${c.id}`}
                      className="bg-purple-500 text-white px-2 py-1 rounded hover:bg-purple-600"
                    >
                      Inscribirse
                    </Link>
                  )}

                  {(c.estado === "Cerrada" || cuposLlenos) && (
                    <span className="bg-gray-400 text-white px-2 py-1 rounded">
                      No disponible
                    </span>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default ListadoConvocatorias;
