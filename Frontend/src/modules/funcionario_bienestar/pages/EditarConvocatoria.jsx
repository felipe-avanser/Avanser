import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const EditarConvocatoria = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [convocatoria, setConvocatoria] = useState(null);

  useEffect(() => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const encontrada = todas.find((c) => c.id === Number(id));
    setConvocatoria(encontrada);
  }, [id]);

  const handleChange = (e) => {
    setConvocatoria({ ...convocatoria, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validación de fechas
    const fechaInicio = new Date(convocatoria.inicio);
    const fechaCierre = new Date(convocatoria.cierre);

    if (fechaCierre <= fechaInicio) {
      alert("❌ La fecha de cierre debe ser posterior a la fecha de inicio.");
      return;
    }

    // Restricciones dinámicas
    const tieneInscripciones = convocatoria.inscripciones?.length > 0;
    const yaComenzo = new Date(convocatoria.inicio) <= new Date();

    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const actualizadas = todas.map((c) =>
      c.id === Number(id) ? { ...convocatoria } : c
    );
    localStorage.setItem("convocatorias", JSON.stringify(actualizadas));

    alert("✅ Convocatoria actualizada exitosamente");
    navigate(`/detalle-convocatoria/${id}`);
  };

  if (!convocatoria) {
    return <div className="p-6 text-center">Convocatoria no encontrada.</div>;
  }

  const tieneInscripciones = convocatoria.inscripciones?.length > 0;
  const yaComenzo = new Date(convocatoria.inicio) <= new Date();

  return (
    <div className="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
      <h2 className="text-2xl font-bold mb-4">Editar Convocatoria</h2>
      <form onSubmit={handleSubmit}>
        <label className="block mb-2 font-semibold">Título</label>
        <input
          type="text"
          name="titulo"
          value={convocatoria.titulo}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Tipo</label>
        <input
          type="text"
          name="tipo"
          value={convocatoria.tipo}
          onChange={handleChange}
          disabled={tieneInscripciones}
          className={`w-full p-2 border rounded mb-4 ${
            tieneInscripciones ? "bg-gray-100" : ""
          }`}
          required
        />

        <label className="block mb-2 font-semibold">Fecha de inicio</label>
        <input
          type="date"
          name="inicio"
          value={convocatoria.inicio}
          onChange={handleChange}
          disabled={yaComenzo}
          className={`w-full p-2 border rounded mb-4 ${
            yaComenzo ? "bg-gray-100" : ""
          }`}
          required
        />

        <label className="block mb-2 font-semibold">Fecha de cierre</label>
        <input
          type="date"
          name="cierre"
          value={convocatoria.cierre}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Cupos disponibles</label>
        <input
          type="number"
          name="cupos"
          value={convocatoria.cupos}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Descripción</label>
        <textarea
          name="descripcion"
          value={convocatoria.descripcion}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-all"
        >
          Guardar cambios
        </button>
      </form>
    </div>
  );
};

export default EditarConvocatoria;
